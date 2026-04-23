---
name: smartthings-cli
description: Query and manage SmartThings devices via CLI, with China region support using --environment flag.
version: 1.0.0
author: community
license: Apache-2.0
metadata:
  hermes:
    tags: [Smart-Home, SmartThings, IoT, Samsung, China-Region]
    homepage: https://github.com/SmartThingsCommunity/smartthings-cli
prerequisites:
  commands: [smartthings]
---

# SmartThings CLI

Command-line interface for managing SmartThings devices, especially for China region users.

## Installation

```bash
npm install -g @smartthings/cli
```

**Requirements:** Node.js >= 22 (or at least 20.x may work with warnings)

## China Region Support

The SmartThings CLI supports both global and China regions. Use the `--environment` flag:

```bash
# Query devices in China region
smartthings devices --environment china

# Query devices in global region (default)
smartthings devices --environment global
```

## Common Commands

### List Devices
```bash
# All devices in China
smartthings devices --environment china

# With verbose output (includes location/room)
smartthings devices --environment china --verbose

# JSON output
smartthings devices --environment china --json

# Filter by capability
smartthings devices --environment china --capability switch

# Filter by device type
smartthings devices --environment china --type zigbee --type zwave
```

### Device Details
```bash
# Get specific device by ID
smartthings devices <device-id> --environment china

# Get device status
smartthings devices:status <device-id> --environment china

# Get device health
smartthings devices:health <device-id> --environment china

# Get device history
smartthings devices:history <device-id> --environment china
```

### Locations & Rooms
```bash
# List locations
smartthings locations --environment china

# List rooms in a location
smartthings locations:rooms <location-id> --environment china
```

### Scenes & Rules
```bash
# List scenes
smartthings scenes --environment china

# Execute a scene
smartthings scenes:execute <scene-id> --environment china

# List rules
smartthings rules --environment china
```

## Configuration

### Config File Location
- **Linux:** `~/.config/@smartthings/cli/config.yaml`
- **MacOS:** `~/Library/Preferences/@smartthings/cli/config.yaml`
- **Windows:** `%LOCALAPPDATA%\@smartthings\cli\config.yaml`

### Set Default Environment
To avoid typing `--environment china` every time, add to config:

```yaml
default:
  environment: china
```

### Multiple Profiles
```yaml
default:
  environment: global

china:
  environment: china
  indent: 2
```

Use with `--profile` flag:
```bash
smartthings devices --profile china
```

## Authentication

### Personal Access Token (PAT)
**China region requires PAT -- browser OAuth is NOT supported.**

1. Go to SmartThings China PAT portal: https://account.samsungiotcloud.cn/tokens
2. Log in with your Samsung account
3. Create a new token with appropriate scopes (devices:r, devices:w, etc.)
4. Add to config:

### Browser Login (Global only)
The CLI automatically opens a browser window for OAuth login on first use. **This only works for the global environment.** If you try `smartthings devices --environment china` without a token, you'll get: `a token is required for the china environment`.

### China Region Token Setup
```yaml
default:
  token: <your-pat-uuid>
  environment: china
```

### Switching from Token to Browser Login
If your config has a `token` set, the CLI will always use it -- `smartthings logout` does NOT clear bearer tokens. To force browser OAuth, you must manually remove the `token` line from config:
```bash
# Delete or edit config
rm ~/.config/@smartthings/cli/config.yaml
# Then run a command for the global environment (China requires PAT)
smartthings devices
```

1. Generate PAT in SmartThings developer portal
2. Add to config:
```yaml
default:
  token: <your-pat-uuid>
  environment: china
```

Or use inline:
```bash
smartthings devices --token <uuid> --environment china
```

## Device Integration Types

Available `--type` filters:
- `ZIGBEE`, `ZWAVE`, `MATTER`
- `LAN`, `MQTT`, `OCF`
- `BLE`, `BLE_D2D`
- `VIRTUAL`, `MOBILE`
- `HUB`, `GROUP`
- `IR`, `IR_OCF`
- `ENDPOINT_APP`, `DTH`
- `PENGYOU`, `SHP`, `VIDEO`, `VIPER`, `WATCH`
- `EDGE_CHILD`

## Troubleshooting

### Node Version Warnings
If you see `EBADENGINE` warnings about Node version:
```bash
# Upgrade Node.js to >= 22
# Or ignore warnings if CLI works
```

### Browser Unavailable on NixOS/IDX
If you try to use `browser_navigate` for the PAT portal on an IDX/NixOS system:
- Playwright installs successfully (`npm install -g @playwright/test && npx playwright install chromium`)
- But Chromium fails at runtime with `error while loading shared libraries: libglib-2.0.so.0`
- `npx playwright install --with-deps` fails because `su: must be run from a terminal`
- Installing glib via `nix-env -iA nixpkgs.glib` doesn't help -- NixOS doesn't use standard `/lib` paths
- **Workaround**: Tell the user to open https://account.samsungiotcloud.cn/tokens in their own browser instead of trying to launch one on the server

### Authentication Issues
```bash
# Note: smartthings logout does NOT clear bearer/PAT tokens in config.yaml.
# To force re-authentication:
# - For global: remove token from config.yaml, then run any command
# - For china: get a new PAT from https://account.samsungiotcloud.cn/tokens

# Force re-login (global only)
smartthings logout
smartthings devices
```

### China Region: No Browser OAuth
The China environment (`--environment china`) does NOT support browser OAuth. It requires a Personal Access Token (PAT) from https://account.samsungiotcloud.cn/tokens. Attempting to use China without a token produces: `a token is required for the china environment`.

**Root cause (from source code):**
In `@smartthings/core-sdk/dist/endpoint-client.js`:
- `globalSmartThingsURLProvider` has `authURL` (`auth-global.api.smartthings.com/oauth/token`) and `keyApiURL`
- `chinaSmartThingsURLProvider` only has `baseURL` (`api.samsungiotcloud.cn`) — **no `authURL`, no `clientId`**

The CLI's `buildAuthenticator()` in `api-command.js` checks `'clientId' in urlProvider` to decide between browser OAuth vs PAT. Since China's provider lacks `clientId`, it falls through to the `fatalError` path.

A comment in the SDK reads: `// When login auth flow is added for China, make authURL required again.` — meaning Samsung has预留 this hook for future OAuth support.

**CLI version check:** As of 2026-04-20, `@smartthings/cli@2.1.1` is the latest version and still has no China OAuth support.

### API Differences
China region uses different API endpoints. Some features available globally may not be available in China region and vice versa.

## Sending Device Commands

### Basic Commands
```bash
# Turn switch on/off
smartthings devices:commands <device-id> switch:on --environment china
smartthings devices:commands <device-id> switch:off --environment china

# Set brightness level
smartthings devices:commands <device-id> 'switchLevel:setLevel(50)' --environment china

# Set color temperature (Kelvin)
smartthings devices:commands <device-id> 'colorTemperature:setColorTemperature(2700)' --environment china
```

### Color Control Commands
**Important**: Use single quotes around the command to prevent shell JSON parsing errors.

```bash
# Set hue (0-360)
smartthings devices:commands <device-id> 'colorControl:setHue(0)' --environment china

# Set saturation (0-100)
smartthings devices:commands <device-id> 'colorControl:setSaturation(100)' --environment china
```

### ⚠️ setColor Command Quirks

The `colorControl:setColor` command has **inconsistent argument formats** depending on device type:

**Format 1** (physical devices like Nanoleaf): `{"color":{"hue":0,"saturation":100}}`
```bash
smartthings devices:commands <device-id> 'colorControl:setColor({"color":{"hue":0,"saturation":100}})' --environment china
```

**Format 2** (virtual lights): `{"hue":0,"saturation":100}` (no nested `color` key)
```bash
smartthings devices:commands <device-id> 'colorControl:setColor({"hue":0,"saturation":100})' --environment china
```

**If setColor fails (422 error)**: Fall back to separate `setHue` and `setSaturation` commands — this is **more reliable** for virtual lights and some Matter devices:

```bash
# Reliable approach for all device types:
smartthings devices:commands <device-id> 'colorControl:setHue(0)' --environment china
smartthings devices:commands <device-id> 'colorControl:setSaturation(100)' --environment china
```

**Color Reference**:
- Red: hue=0, saturation=100
- Green: hue=120, saturation=100
- Blue: hue=240, saturation=100
- Warm yellow: hue=50, saturation=80 (or use colorTemperature:2700)

## Useful One-liners

⚠️ **JSON Processing**: `python3` and `jq` may not be available on this system. Use `node -e` for JSON processing:

```bash
# List devices with label, type, location, room
smartthings devices --environment china --json | node -e "
const chunks=[]; process.stdin.on('data',d=>chunks.push(d));
process.stdin.on('end',()=>{
  const data=JSON.parse(Buffer.concat(chunks));
  data.forEach((d,i)=>console.log(\`\${i+1}. \${d.label} | \${d.type} | \${d.location} / \${d.room}\`));
});
"

# Count devices by type
smartthings devices --environment china --json | node -e "
const chunks=[]; process.stdin.on('data',d=>chunks.push(d));
process.stdin.on('end',()=>{
  const data=JSON.parse(Buffer.concat(chunks));
  const counts={}; data.forEach(d=>counts[d.type]=(counts[d.type]||0)+1);
  console.log(counts);
});
"
```

# List all switch devices
smartthings devices --environment china --capability switch --json | jq '.[].label'

# Export device list to file
smartthings devices --environment china --json > devices.json
```

### ⚠️ Why China Requires PAT (Code-Level Analysis)
The `chinaSmartThingsURLProvider` in `@smartthings/core-sdk` only defines `baseURL` (`https://api.samsungiotcloud.cn`) — it is missing `authURL` and `clientId`. The CLI checks `'clientId' in urlProvider` to trigger browser OAuth. Since China's provider lacks it, the CLI falls back to: `fatalError('a token is required for the china environment')`. The SDK source explicitly comments: `// When login auth flow is added for China, make authURL required again.` This confirms the OAuth endpoints are simply not provisioned on the China backend yet.

### ⚠️ Common Pitfalls & Observations

### 1. Virtual vs Physical Devices
Many devices in SmartThings are **Virtual** (`type: "VIRTUAL"`). 
- They accept commands and update state successfully.
- **However, they have no physical effect** (no actual light turns on).
- Always check `type` in device details if the user complains "it didn't work" despite a successful command.

### 2. Location/Room Confusion
- Device labels (e.g., "顶灯1") can be duplicated across different rooms (e.g., Living Room vs Dining Room).
- **Always verify the `roomId` and room name** before executing commands if multiple devices share the same label.

### 3. Bulk Command Permissions (403 Forbidden)
- When executing bulk commands across many devices, you may get **403 Forbidden** for some.
- This usually happens when devices belong to **different Locations** (e.g., "Existing user" location) or are managed by a different Hub/Account that the current CLI profile doesn't have write access to.
- Use `;` instead of `&&` when chaining commands to ensure execution continues for authorized devices even if one fails.

## Related Resources

- GitHub: https://github.com/SmartThingsCommunity/smartthings-cli
- API Docs: https://developer.smartthings.com/docs/api/public/
- Core SDK: https://github.com/SmartThingsCommunity/smartthings-core-sdk
