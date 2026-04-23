---
name: appliance-fault-diagnosis
description: Diagnose home appliance faults using local knowledge base before searching external sources
version: 1.0.0
metadata:
  hermes:
    tags: [appliance, refrigerator, fault-codes, knowledge-base, troubleshooting]
---

# Appliance Fault Diagnosis with Local Knowledge Base

When users report appliance problems (especially refrigerators), **always check the local knowledge base first** before searching externally.

## Knowledge Base Location

```
~/mydocs/knowledgebase/
```

## Available Resources

### Text Files
- `家电维修.txt` - Contains fault codes and descriptions

### PDF Manuals (VERIFIED CONTENTS)

| Filename | Actual Content | Pages |
|----------|----------------|-------|
| `BN81-27185G-690_EUG_ROPDVBCNF_CN_S-CHI_250818.0.pdf` | **Samsung TV** user manual | 254 |
| `DA68-04798R-06_RF8500_Defeature_CN_SVC.pdf` | **Samsung Refrigerator RF50DG5021** user manual | 46 |
| `DB68-12848B-01_QG_FAC_MEMORY_SC_ZH-CH_2026.03.17.pdf` | **Samsung AC (Air Conditioner)** quick guide | 16 |
| `OID78248_IB_T-PJT_WD8000D_7LCD_ZH-CN_260113.pdf` | **Samsung WD8000D Washing Machine** manual | (unverified) |

⚠️ **Critical Lesson**: PDF filenames may NOT match content (e.g., "RF8500" filename contains RF50DG5021 refrigerator manual). **Always verify by extracting first few pages before referencing.**

## Workflow

### Step 1: List Knowledge Base Contents
```bash
ls -la ~/hermes-agent/mydocs/knowledgebase/
```
**Note**: Path is `~/hermes-agent/mydocs/knowledgebase/` (relative to hermes-agent directory).

### Step 2: Read Fault Code Reference (TEXT FILE FIRST)
```bash
cat ~/hermes-agent/mydocs/knowledgebase/家电维修.txt
```
Contains basic fault codes for refrigerators (C71, C72, C73, C76).

### Step 3: Search PDF Manuals for Detailed Information

**Install pymupdf if needed:**
```bash
~/hermes-agent/venv/bin/python -m pip install pymupdf -q
```

**Extract and verify PDF content (first 30 pages):**
```python
import pymupdf

# Use absolute path
doc = pymupdf.open("/home/user/hermes-agent/mydocs/knowledgebase/<filename>.pdf")

# Extract first 30 pages to identify content
text = ""
for i, page in enumerate(doc[:30]):
    text += f"\n=== 第 {i+1} 页 ===\n"
    text += page.get_text()

print(text[:15000])  # Limit output
print(f"\n\n总页数：{len(doc)}")
```

**Search for specific content (error codes, symptoms):**
```python
import pymupdf

doc = pymupdf.open("/home/user/hermes-agent/mydocs/knowledgebase/<filename>.pdf")

# Search all pages for keywords
for i, page in enumerate(doc):
    text = page.get_text()
    if "高温" in text or "报警" in text or "错误" in text:
        print(f"\n=== 第 {i+1} 页 ===")
        print(text[:2000])
```

**Extract specific sections (e.g., pages 39-46 for troubleshooting):**
```python
import pymupdf

doc = pymupdf.open("/home/user/hermes-agent/mydocs/knowledgebase/<filename>.pdf")

text = ""
for i, page in enumerate(doc[38:46]):  # Pages 39-46 (0-indexed)
    text += f"\n=== 第 {i+39} 页 ===\n"
    text += page.get_text()

print(text[:12000])
```

### Step 4: Provide Troubleshooting Steps

**From `家电维修.txt` (basic fault codes):**

| Code | Fault | Solution |
|------|-------|----------|
| C71 | 冷冻室高温检测 | Check freezer door closed, no hot food stored |
| C72 | 冷藏室高温检测 | Check refrigerator door closed, no hot food stored |
| C73 | 整个冰箱高温检测 | Check all doors closed |
| C76 | 自动注水溢出错误 | Remove rubber plug from water bucket bottom, drain, replace plug |

**From Refrigerator Manual (DA68-04798R-06) - Comprehensive Troubleshooting:**

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| 冷藏室/冷冻室不工作 | 电源线未正确插入 | 正确插入电源线 |
| 冷藏室/冷冻室温度高 | 温度控制设置偏高 | 设置更低温度 |
| 冷藏室/冷冻室温度高 | 冰箱靠近热源或阳光直射 | 让冰箱远离阳光直射或热源 |
| 冷藏室/冷冻室温度高 | 冰箱过载，食物挡住通风口 | 请勿过载冰箱，请勿让食物挡住通风口 |
| 冷藏室/冷冻室过度制冷 | 温度控制设置偏低 | 设置更高温度 |
| 箱口发热 | 防露管正常工作 | 非故障，正常现象 |
| 冰箱有异味 | 食物变质 | 清洁冰箱，取出变质食物 |
| 冰箱有异味 | 有强烈气味的食物 | 确保紧紧包裹有强烈气味的食物 |
| 通风口周围结霜 | 食物挡住通风口 | 确保没有食物挡住通风口 |
| 内壁结霜 | 关门有缝隙 | 确保食物没挡住门，清洁门垫圈 |
| 内壁冷凝 | 门保持打开，湿气进入 | 排出湿气，勿长时间开门 |
| 内壁冷凝 | 含大量水分的食物 | 确保紧紧包裹食物 |

**Samsung Customer Service**: 400-810-5858 (all Samsung appliances)

## Response Template

When user reports a fault code:

1. **Confirm the fault code** and its meaning from knowledge base
2. **Provide step-by-step troubleshooting**:
   - Check doors/seals
   - Check stored items (no hot food)
   - Check ventilation (no blockage)
   - Check temperature settings
   - Wait 2-4 hours for recovery
   - Contact service if problem persists
3. **Ask for appliance model** to look up specific manual if needed
4. **Provide relevant technical specs** if user asks (capacity, dimensions, power, etc.)

## Samsung Refrigerator RF50DG5021 Quick Reference

**Models**: RF50DG5021CWSC, RF50DG5021EMSC

| Parameter | Value |
|-----------|-------|
| Total Capacity | 501 L |
| Refrigerator | 325 L (1~7℃) |
| Freezer | 88 L (-23~-15℃) |
| Multi-Zone | 88 L (-23~3℃) |
| Dimensions | 834×600×1920 mm (W×D×H) |
| Power | 220V~/50Hz, 2.5A, 170W |
| Refrigerant | R-600a / 86g |
| Energy Rating | Level 1 |
| Noise | 36 dB(A) |
| Annual Consumption | 361 kW·h/y |

**Temperature Settings**:
- Refrigerator: 1~7℃ (default ~3℃)
- Freezer: -23~-15℃ (default -19℃)
- Multi-Zone modes: Freezer (-23~-15℃), Soft Freeze (-3℃), Meat/Fish (-1℃), Fruit/Veg (2℃), Beverage (3℃), Grain/Tea (3℃)

**Smart Features**: SmartThings app support, Wi-Fi (2.4GHz), Ion Deodorization (model dependent)

## Key Questions to Ask User

1. What fault code is displayed?
2. What is the specific problem? (not cooling, too warm, leaking, no power)
3. What is the appliance model number?

## Extracting Images from PDF Manuals

**Extract all embedded images (diagrams, installation figures):**

```python
import pymupdf
import os

pdf_path = "/home/user/hermes-agent/mydocs/knowledgebase/<filename>.pdf"
output_dir = "/home/user/hermes-agent/mydocs/knowledgebase/images"

os.makedirs(output_dir, exist_ok=True)
doc = pymupdf.open(pdf_path)

image_count = 0
for page_num in range(len(doc)):
    page = doc[page_num]
    image_list = page.get_images(full=True)
    
    if image_list:
        print(f"第 {page_num + 1} 页 找到 {len(image_list)} 张图片")
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            filename = f"{output_dir}/<prefix>_p{page_num+1}_img{img_index+1}.{image_ext}"
            with open(filename, "wb") as f:
                f.write(image_bytes)
            image_count += 1

print(f"✅ 总共提取 {image_count} 张图片")
```

**Typical image locations in refrigerator manual:**
- Page 1: Product外观图, Logo
- Page 18: 安装尺寸图，空间要求示意图 (8 images)
- Page 21-22: 垫板使用方法，止动块安装图，插座位置图 (26 images)
- Page 33: 控制面板示意图

## Creating ASCII Diagrams (when matplotlib Chinese fonts unavailable)

**Matplotlib Chinese font issue:**
```python
# Will produce warnings like:
# UserWarning: Glyph 20919 (\N{CJK UNIFIED IDEOGRAPH-51B7}) missing from font(s) DejaVu Sans
```

**Fallback: Use ASCII art for structural diagrams:**
```
╔══════════════════════════════════════════════════════════╗
║         三星冰箱 RF50DG5021 内部结构示意图                ║
╠══════════════════════════════════════════════════════════╣
║  ┌────────────────────────────────────────────────────┐  ║
║  │              冷藏室 (325L) 1~7℃                   │  ║
║  │  ┌────────────────────────────────────────────┐    │  ║
║  │  │  ████████████████████████████████████████ │搁板│  ║
║  │  └────────────────────────────────────────────┘    │  ║
║  │  ┌──────────────┐  ┌──────────────┐               │  ║
║  │  │  抽屉        │  │  抽屉        │               │  ║
║  │  └──────────────┘  └──────────────┘               │  ║
║  └────────────────────────────────────────────────────┘  ║
║  ┌────────────────────────────────────────────────────┐  ║
║  │           变温室 (88L) -23℃~3℃                     │  ║
║  └────────────────────────────────────────────────────┘  ║
║  ┌────────────────────────────────────────────────────┐  ║
║  │           冷冻室 (88L) -23℃~-15℃                   │  ║
║  └────────────────────────────────────────────────────┘  ║
╚══════════════════════════════════════════════════════════╝
```

## Important Notes

- **Always check knowledge base FIRST** - user prefers local documentation before web search
- **PDF filenames may NOT match content** - verified: "RF8500" filename contains RF50DG5021 refrigerator manual
  - This is a critical lesson: Never trust PDF filenames alone
  - Always extract first 30 pages to verify actual content before referencing
- **Use absolute paths** for PDF extraction: `/home/user/hermes-agent/mydocs/knowledgebase/`
- **Install pymupdf** for PDF text extraction: `~/hermes-agent/venv/bin/python -m pip install pymupdf -q`
- **Extract systematically**: First 30 pages for content ID, then search for keywords, then extract specific sections
- **Fault codes are model-specific** - verify against correct manual
- **Some issues resolve automatically** after 2-4 hours if door was left open or hot food was stored
- **Normal sounds** (clicking, buzzing, hissing, bubbling, cracking) are NOT faults - educate users
- **Samsung Customer Service**: 400-810-5858 (applicable to all Samsung appliances)
- **High humidity condensation** (回南天，梅雨季节) on exterior is normal - will disappear automatically
- **Images can be extracted** from PDFs for diagrams (36 images in refrigerator manual)
- **ASCII art fallback** when matplotlib lacks Chinese font support
- **Knowledge base path**: `~/hermes-agent/mydocs/knowledgebase/` (relative to hermes-agent project directory)

## Samsung AC Troubleshooting & Maintenance
**Manual**: `DB68-12848B-01_QG_FAC_MEMORY_SC_ZH-CH_2026.03.17.pdf` (16 pages)

### Odor / Bad Smell from Vent
1. **Clean Filters**:
   - **Air filter**: Vacuum dust or rinse with water.
   - **"Four Seasons Purification" filter**: Soak in water, wash with neutral detergent. ⚠️ **DO NOT USE BRUSHES** (will damage filter). Dry vertically in shade for **>12 hours**. ☀️ **NO DIRECT SUNLIGHT** (causes deformation).
2. **Enable Anti-Mold (防霉)**: On remote, press `功能` → select `防霉` (or hold 3s). Keeps fan running after shutdown to dry internal moisture and prevent mold/odor.
3. **Smart Clean**: Some models support automatic internal cleaning cycles.
4. **Reset Filter Reminder**: Hold `净化` (Purify) or filter-icon button for 3s after reinstalling.
5. **Deep Clean**: If odor persists (sour/musty), evaporator coil likely has mold. Use AC coil cleaner or call professional for steam cleaning.

### PDF Extraction Tip
Use `pymupdf` to search keywords: `异味`, `清洁`, `过滤网`, `防霉` in the AC manual.
