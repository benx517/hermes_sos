#!/usr/bin/env python3
"""Extract text from documents using pymupdf. Lightweight (~25MB), no models.

Usage:
    python extract_pymupdf.py document.pdf
    python extract_pymupdf.py document.pdf --markdown
    python extract_pymupdf.py document.pdf --pages 0-4
    python extract_pymupdf.py document.pdf --images output_dir/
    python extract_pymupdf.py document.pdf --tables
    python extract_pymupdf.py document.pdf --metadata
    python extract_pymupdf.py document.pdf --render output_dir/              # Render all pages as 2x PNG
    python extract_pymupdf.py document.pdf --render output_dir/ --pages 0-4  # Render specific pages
    python extract_pymupdf.py document.pdf --all output_dir/                 # → full_text.txt + metadata.json + renders/
    python extract_pymupdf.py document.pdf --all output_dir/ --no-cache      # Force re-parse even if cached
"""
import sys
import json

# PyMuPDF compatibility: older versions (≤1.23.x) use `import fitz`,
# newer versions (≥1.24.x) use `import pymupdf`. Try both.
try:
    import pymupdf
    # Old versions may ship a namespace package that imports but lacks 'open'
    if not hasattr(pymupdf, 'open'):
        raise AttributeError
except (ImportError, AttributeError):
    import fitz as pymupdf


def extract_text(path, pages=None):
    doc = pymupdf.open(path)
    page_range = range(len(doc)) if pages is None else pages
    for i in page_range:
        if i < len(doc):
            print(f"\n--- Page {i+1}/{len(doc)} ---\n")
            print(doc[i].get_text())

def extract_markdown(path, pages=None):
    import pymupdf4llm
    md = pymupdf4llm.to_markdown(path, pages=pages)
    print(md)

def extract_tables(path):
    doc = pymupdf.open(path)
    for i, page in enumerate(doc):
        tables = page.find_tables()
        for j, table in enumerate(tables.tables):
            print(f"\n--- Page {i+1}, Table {j+1} ---\n")
            df = table.to_pandas()
            print(df.to_markdown(index=False))

def extract_images(path, output_dir):
    from pathlib import Path
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(path)
    count = 0
    for i, page in enumerate(doc):
        for img_idx, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            smask = img[1] if len(img) > 1 else 0
            pix = pymupdf.Pixmap(doc, xref)
            # If the image has a soft mask (transparency), combine it
            if smask:
                mask = pymupdf.Pixmap(doc, smask)
                pix = pymupdf.Pixmap(pix, mask) if pix.alpha else pix
            # Convert CMYK (n >= 4 without alpha, n >= 5 with alpha) to RGB
            if pix.n - pix.alpha >= 4:
                pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
            out_path = f"{output_dir}/page{i+1}_img{img_idx+1}.png"
            pix.save(out_path)
            count += 1
    print(f"Extracted {count} images to {output_dir}/")

def render_pages(path, output_dir, pages=None):
    """Render PDF pages as 2x PNG images for vision analysis."""
    from pathlib import Path
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(path)
    page_range = range(len(doc)) if pages is None else pages
    count = 0
    for i in page_range:
        if i < len(doc):
            page = doc[i]
            pix = page.get_pixmap(matrix=pymupdf.Matrix(2, 2))
            out_path = f"{output_dir}/page{i+1:02d}_render.png"
            pix.save(out_path)
            count += 1
    print(f"Rendered {count} pages to {output_dir}/")
    doc.close()

def _cache_key(path):
    """Compute a cache key from the PDF file's path, size, and mtime."""
    import os
    st = os.stat(path)
    return f"{os.path.abspath(path)}|{st.st_size}|{st.st_mtime}"

def extract_all(path, output_dir, pages=None, no_cache=False):
    """Run text + metadata + renders in one pass. Saves files to output_dir.
    Skips parsing if output_dir already contains valid cached results.
    Use --images separately for embedded images."""
    from pathlib import Path
    renders_dir = f"{output_dir}/renders"
    cache_key_file = f"{output_dir}/.cache_key"

    # Cache check
    if not no_cache and Path(cache_key_file).exists():
        current_key = _cache_key(path)
        stored_key = Path(cache_key_file).read_text(encoding="utf-8").strip()
        if current_key == stored_key and Path(f"{output_dir}/full_text.txt").exists():
            print(json.dumps({
                "output_dir": output_dir,
                "metadata": f"{output_dir}/metadata.json",
                "text": f"{output_dir}/full_text.txt",
                "renders": renders_dir,
                "cached": True,
            }, indent=2))
            return

    Path(renders_dir).mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(path)
    page_range = range(len(doc)) if pages is None else pages

    # Metadata → metadata.json
    meta = {
        "pages": len(doc),
        "title": doc.metadata.get("title", ""),
        "author": doc.metadata.get("author", ""),
        "subject": doc.metadata.get("subject", ""),
        "creator": doc.metadata.get("creator", ""),
        "producer": doc.metadata.get("producer", ""),
        "format": doc.metadata.get("format", ""),
    }
    with open(f"{output_dir}/metadata.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    # Text + renders
    all_text_parts = []
    render_count = 0
    for i in page_range:
        if i >= len(doc):
            continue
        page = doc[i]
        text = page.get_text()
        all_text_parts.append(f"--- Page {i+1}/{len(doc)} ---\n{text}")

        render_pix = page.get_pixmap(matrix=pymupdf.Matrix(2, 2))
        render_pix.save(f"{renders_dir}/page{i+1:02d}_render.png")
        render_count += 1

    doc.close()

    # Text → full_text.txt
    with open(f"{output_dir}/full_text.txt", "w", encoding="utf-8") as f:
        f.write("\n\n".join(all_text_parts))

    # Write cache key
    Path(cache_key_file).write_text(_cache_key(path), encoding="utf-8")

    print(json.dumps({
        "output_dir": output_dir,
        "metadata": f"{output_dir}/metadata.json",
        "text": f"{output_dir}/full_text.txt",
        "renders": renders_dir,
        "pages_rendered": render_count,
        "text_chars": sum(len(p) for p in all_text_parts),
        "cached": False,
    }, indent=2))

def show_metadata(path):
    doc = pymupdf.open(path)
    print(json.dumps({
        "pages": len(doc),
        "title": doc.metadata.get("title", ""),
        "author": doc.metadata.get("author", ""),
        "subject": doc.metadata.get("subject", ""),
        "creator": doc.metadata.get("creator", ""),
        "producer": doc.metadata.get("producer", ""),
        "format": doc.metadata.get("format", ""),
    }, indent=2))

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    path = args[0]
    pages = None

    if "--pages" in args:
        idx = args.index("--pages")
        p = args[idx + 1]
        if "-" in p:
            start, end = p.split("-")
            pages = list(range(int(start), int(end) + 1))
        else:
            pages = [int(p)]

    if "--metadata" in args:
        show_metadata(path)
    elif "--tables" in args:
        extract_tables(path)
    elif "--images" in args:
        idx = args.index("--images")
        output_dir = args[idx + 1] if idx + 1 < len(args) else "./images"
        extract_images(path, output_dir)
    elif "--render" in args:
        idx = args.index("--render")
        output_dir = args[idx + 1] if idx + 1 < len(args) else "./renders"
        render_pages(path, output_dir, pages=pages)
    elif "--all" in args:
        idx = args.index("--all")
        output_dir = args[idx + 1] if idx + 1 < len(args) else "./pdf_output"
        extract_all(path, output_dir, pages=pages, no_cache="--no-cache" in args)
    elif "--markdown" in args:
        extract_markdown(path, pages=pages)
    else:
        extract_text(path, pages=pages)
