#!/usr/bin/env python3
"""
Fetch SmartThings compatible devices catalog data from Samsung's GraphQL API.
Outputs all super categories, categories, and brands as JSON or markdown table.

Usage:
    python fetch_catalog.py [--region china|global] [--format json|markdown]
"""

import argparse
import json
import ssl
import urllib.request
import urllib.error

ENDPOINTS = {
    "china": "https://api.samsungiotcloud.cn/catalogs/api/v3/malls/graphql",
    "global": "https://api.smartthings.com/catalogs/api/v3/malls/graphql",
}


def fetch(query: str, region: str = "china") -> dict:
    url = ENDPOINTS[region]
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    data = json.dumps({"query": query}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    response = urllib.request.urlopen(req, context=ctx, timeout=15)
    result = json.loads(response.read().decode("utf-8"))
    if "errors" in result:
        print(f"GraphQL errors: {result['errors']}")
    return result.get("data", {})


def get_super_categories(region: str = "china") -> list:
    query = """
    query {
      allSuperCategories {
        totalCount
        superCategories {
          id
          name
          localizations { locale displayName }
          childCategoryIds
        }
      }
    }
    """
    data = fetch(query, region)
    return data.get("allSuperCategories", {}).get("superCategories", [])


def get_all_categories(region: str = "china") -> list:
    all_cats = []
    page = 0
    while True:
        query = f"""
        query {{
          allCategories(pageNumber: {page}, pageSize: 100) {{
            totalCount
            pageInfo {{ hasNextPage }}
            categories {{
              id uuid name iconUrl
              localizations {{ locale displayName }}
              superCategoryIds
            }}
          }}
        }}
        """
        data = fetch(query, region)
        cats = data.get("allCategories", {}).get("categories", [])
        all_cats.extend(cats)
        page_info = data.get("allCategories", {}).get("pageInfo", {})
        if not page_info.get("hasNextPage", False):
            break
        page += 1
    return all_cats


def get_all_brands(region: str = "china") -> list:
    all_brands = []
    page = 0
    while True:
        query = f"""
        query {{
          allBrands(pageNumber: {page}, pageSize: 100) {{
            totalCount
            brands {{ id name }}
          }}
        }}
        """
        data = fetch(query, region)
        brands = data.get("allBrands", {}).get("brands", [])
        all_brands.extend(brands)
        # Simple pagination - assume < 500 brands
        if len(brands) < 100:
            break
        page += 1
    return all_brands


def localize(item: dict, fallback: str = None) -> str:
    """Get localized display name (prefer Chinese, fallback to name)."""
    for loc in item.get("localizations", []):
        if loc.get("locale", "").startswith("zh"):
            return loc.get("displayName", "")
    return fallback or item.get("name", "")


def main():
    parser = argparse.ArgumentParser(description="Fetch SmartThings catalog data")
    parser.add_argument("--region", choices=["china", "global"], default="china")
    parser.add_argument("--format", choices=["json", "markdown", "table"], default="table")
    args = parser.parse_args()

    print(f"Fetching SmartThings catalog ({args.region} region)...")

    super_cats = get_super_categories(args.region)
    categories = get_all_categories(args.region)
    brands = get_all_brands(args.region)

    if args.format == "json":
        output = {
            "region": args.region,
            "superCategories": super_cats,
            "categories": categories,
            "brands": brands,
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return

    # Super Categories
    if args.format == "markdown":
        print("### Super Categories\n")
        print("| ID | Name | Child Count |")
        print("|----|------|-------------|")
        for sc in super_cats:
            name = localize(sc)
            print(f"| {sc['id']} | {name} | {len(sc.get('childCategoryIds', []))} |")

        print(f"\n### Categories ({len(categories)} total)\n")
        print("| ID | Name | Super Categories |")
        print("|----|------|-----------------|")
        for cat in categories:
            name = localize(cat)
            supers = ", ".join(str(x) for x in cat.get("superCategoryIds", []))
            print(f"| {cat['id']} | {name} | {supers} |")

        print(f"\n### Brands ({len(brands)} total)\n")
        print("| ID | Name |")
        print("|----|------|")
        for b in brands:
            print(f"| {b['id']} | {b['name']} |")

    else:
        print(f"\n=== Super Categories ({len(super_cats)}) ===")
        for sc in super_cats:
            name = localize(sc)
            print(f"  ID:{sc['id']} {name} (children: {len(sc.get('childCategoryIds', []))})")

        print(f"\n=== Categories ({len(categories)} total) ===")
        for cat in categories:
            name = localize(cat)
            supers = cat.get("superCategoryIds", [])
            print(f"  ID:{cat['id']} {name} -> {supers}")

        print(f"\n=== Brands ({len(brands)} total) ===")
        for b in brands:
            print(f"  ID:{b['id']} {b['name']}")


if __name__ == "__main__":
    main()
