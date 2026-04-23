---
name: smartthings-catalog-api
description: Query Samsung SmartThings compatible devices catalog via GraphQL API — fetch all categories, super categories, brands, and products for China and global regions.
version: 1.0.0
author: hermes-agent
license: Apache-2.0
metadata:
  hermes:
    tags: [Smart-Home, SmartThings, Catalog, GraphQL, Samsung, API, China-Region]
prerequisites:
  commands: [curl]
---

# SmartThings Catalog API

Query the Samsung SmartThings compatible devices catalog directly via GraphQL, without needing a browser. Works for both China and global regions.

## Discovery Method

The SmartThings compatible devices page (e.g. `samsung.com.cn/smartthings/compatible-devices/`) uses an embedded React frontend that calls a GraphQL API. The API endpoints are hardcoded in the page JavaScript.

**China region endpoint:**
```
https://api.samsungiotcloud.cn/catalogs/api/v3/malls/graphql
```

**Global region endpoint:**
```
https://api.smartthings.com/catalogs/api/v3/malls/graphql
```

## GraphQL Queries

### 1. Get All Super Categories

```json
{
  "query": "query { allSuperCategories { totalCount superCategories { id name localizations { locale displayName } childCategoryIds } } }"
}
```

### 2. Get All Categories (paginated)

```json
{
  "query": "query allCategories { allCategories(pageNumber: 0, pageSize: 100) { totalCount pageInfo { hasNextPage hasPreviousPage currentPage totalPages } categories { id uuid name iconUrl localizations { locale displayName } dossierCategoryNames superCategoryIds } } }"
}
```

Pagination: use `pageNumber: 1, pageSize: 100` for page 2, etc. Check `pageInfo.hasNextPage`.

### 3. Get All Brands (paginated)

```json
{
  "query": "query allBrands { allBrands(pageNumber: 0, pageSize: 100) { totalCount brands { id name } } }"
}
```

### 4. Get Brands for Specific Categories

```json
{
  "query": "query allBrands($categoryFilter: CategoryFilter) { allBrands(pageNumber: 0, pageSize: 100, filter: $categoryFilter) { totalCount brands { id name } } }",
  "variables": {
    "categoryFilter": {
      "filterByProductCatalog": {
        "categoryIds": [31, 36, 38]
      }
    }
  }
}
```

### 5. Search Products

⚠️ **IMPORTANT (Verified 2026-04-21)**: The API schema has changed. The following filters are **INVALID** and will cause validation errors:
- `filterByProductCatalog` (not a valid field on `ProductCatalogFilter`)
- `searchBy` argument (removed from `allProductCatalogs`)

**Working basic query:**
```json
{
  "query": "query { allProductCatalogs(pageNumber: 0, pageSize: 20) { totalCount productCatalogs { id modelName modelCode } } }"
}
```

**To find specific products** (e.g., Samsung refrigerators), you must **scan all products** and filter client-side:
```json
{
  "query": "query { allProductCatalogs(pageNumber: 0, pageSize: 50) { totalCount productCatalogs { id modelName modelCode localizations { locale shopDisplayName } } } }"
}
```
Total catalog has ~2483 products. Use pagination (`pageNumber`, `pageSize`) and filter results by `modelName` patterns (e.g., `RF*` for refrigerators, `WW*` for washers).

**Alternative: Use categories first, then correlate:**
Get category ID 36 (冰箱), then scan products looking for models matching Samsung fridge patterns.

## Shell Usage

```bash
# Fetch all categories (China)
curl -s -X POST "https://api.samsungiotcloud.cn/catalogs/api/v3/malls/graphql" \
  -H "Content-Type: application/json" \
  -d '{"query":"query allCategories { allCategories(pageNumber: 0, pageSize: 100) { totalCount categories { id uuid name localizations { locale displayName } superCategoryIds } } }"}' | jq .

# Fetch all brands (China)
curl -s -X POST "https://api.samsungiotcloud.cn/catalogs/api/v3/malls/graphql" \
  -H "Content-Type: application/json" \
  -d '{"query":"query allBrands { allBrands(pageNumber: 0, pageSize: 100) { totalCount brands { id name } } }"}' | jq .

# Fetch super categories
curl -s -X POST "https://api.samsungiotcloud.cn/catalogs/api/v3/malls/graphql" \
  -H "Content-Type: application/json" \
  -d '{"query":"query { allSuperCategories { totalCount superCategories { id name localizations { locale displayName } childCategoryIds } } }"}' | jq .

# Fetch product catalog (basic, no filter support verified)
curl -s -X POST "https://api.samsungiotcloud.cn/catalogs/api/v3/malls/graphql" \
  -H "Content-Type: application/json" \
  -d '{"query":"{ allProductCatalogs(pageNumber: 0, pageSize: 20) { totalCount productCatalogs { id modelName modelCode } } }"}' | jq .

## 14 Super Categories (China Region)

| ID | Name (CN) | Key Sub-Category IDs |
|----|-----------|---------------------|
| 1 | 家用电器 | 31(洗衣机), 44(烘干机), 48(扫地机器人), 32(AirDresser) |
| 2 | 智能网关与连接 | 4(WLAN/集线器), 66(桥接器), 85(中继器) |
| 3 | 套件 | 37(ADT安全装置) |
| 4 | 厨房电器 | 36(冰箱), 7(洗碗机), 83(微波炉), 17(烤箱), 72(咖啡机) |
| 5 | 生活方式与其他 | 64(宠物喂食器), 110(猫砂盆), 73(EV充电器), 3(车库门) |
| 6 | 照明与能源 | (空壳大类) |
| 7 | 个人设备 | 92(手表), 111(智能戒指), 78(耳机) |
| 8 | 传感器与安全 | 34(门锁), 25(摄像头), 39(动作感应器), 124(温湿度传感器) |
| 9 | 电视与娱乐 | 41(电视), 57(投影机), 29(扬声器) |
| 10 | 用电 | 23(能耗监视), 26(恒温器), 52(插座) |
| 11 | 照明和开关 | 49(照明), 20(开关/调光器), 71(吊灯) |
| 12 | 空气护理设备 | 38(空调), 43(空气净化器), 18(加湿器), 75(抽湿机) |
| 13 | 可穿戴设备 | 92(手表), 111(智能戒指) |
| 14 | 健身与健康 | 107(体重秤), 61(健身垫) |

**Totals: 14 super categories, 140+ sub-categories, 52 brands**

## Category IDs Reference (China Region)

| Category Name | ID | Super Category |
|--------------|----|---------------|
| 冰箱 | 36 | 厨房电器(4) |
| 洗衣机 | 31 | 家用电器(1) |
| 空调 | 38 | 空气护理设备(12) |
| 电视 | 41 | 电视与娱乐(9) |
| 扫地机器人 | 48 | 家用电器(1) |
| 门锁 | 34 | 传感器与安全(8) |
| 空气净化器 | 43 | 空气护理设备(12) |
| 加湿器 | 18 | 空气护理设备(12) |
| 照明 | 49 | 照明和开关(11) |
| 开关/调光器 | 20 | 照明和开关(11) |
| 温湿度传感器 | 124 | (none) |
| 宠物喂食器 | 64 | 生活方式与其他(5) |
| EV充电器 | 73 | 生活方式与其他(5) |

## Key Brand IDs

| Brand | ID |
|-------|----|
| Samsung | 15 |
| Aqara | 22 |
| Yeelight | 24 |
| Philips Hue | 32 |
| Nanoleaf | 33 |
| Aeotec | 16 |
| ORVIBO | 1 |
| PETKIT | 30 |
| EZVIZ(萤石) | 48 |

## ⚠️ Pitfalls

1. **SSL verification**: The China API may have certificate issues in some environments. Use `ssl.CERT_NONE` or `curl -k` if needed.

2. **Browser not needed**: Playwright/browser automation will fail on Samsung pages due to complex React rendering and lazy loading. The GraphQL API is much faster and more reliable.

3. **Localization**: Category/brand names come in multiple locales. The Chinese display name is typically in the `localizations` array where `locale` starts with `"zh"` or `"zh-CN"`. Fall back to the `name` field if no Chinese localization exists.

4. **Product filtering NOT supported**: As of 2026-04-21, `allProductCatalogs` does NOT accept `filter` or `searchBy` arguments. The `filterByProductCatalog` input type either doesn't exist or has a different structure. You must fetch products in batches and filter client-side.

5. **Filtered categories**: The Samsung web page hides certain categories from search (扫地机器人, 热水器, 空调, 空气净化器, 通风/换气, 声响, 坐便器, 浴霸). These are filtered in frontend JavaScript, NOT by the API — the API returns them normally.

6. **Category ID 43 hidden**: The page also hides `data-category-id="43"` and `"38"` via jQuery. Again, these are frontend-only filters.

7. **No authentication required**: The catalog API is public — no API key or token needed.

8. **Introspection may fail**: The `__type` introspection query returned `'data'` key errors in testing. If schema introspection fails, use trial-and-error with minimal queries to discover valid fields/arguments.

## Python Example

```python
import urllib.request, ssl, json

url = "https://api.samsungiotcloud.cn/catalogs/api/v3/malls/graphql"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

query = '{"query":"query allCategories { allCategories(pageNumber: 0, pageSize: 100) { totalCount categories { id uuid name localizations { locale displayName } superCategoryIds } } }"}'
req = urllib.request.Request(url, data=query.encode(), headers={"Content-Type": "application/json"})
response = urllib.request.urlopen(req, context=ctx, timeout=15)
data = json.loads(response.read())

for cat in data["data"]["allCategories"]["categories"]:
    name = cat["name"]
    for loc in cat.get("localizations", []):
        if loc.get("locale", "").startswith("zh"):
            name = loc.get("displayName", name)
            break
    print(f"ID:{cat['id']} {name}")
```

## Related Skills

- `smartthings-cli` — CLI tool for managing SmartThings devices
- `appliance-fault-diagnosis` — Diagnose appliance faults from local knowledge base