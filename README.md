**Language:** **English** · [Русский](README.ru.md)

# wash-module-starter

WASH PRO CRM module template for building custom extensions.

## Quick start

```bash
git clone https://github.com/WASH-PRO/wash-module-starter my-wash-module
cd my-wash-module
# 1. Change id/name in wash-module.json
# 2. Implement logic in src/main.py
# 3. Configure ui/index.html
```

## Files

| File | Purpose |
|------|---------|
| `wash-module.json` | Manifest for the CRM catalog |
| `src/main.py` | Daemon (PyOrchestrator) |
| `ui/index.html` | Settings page (iframe in Dashboard) |
| `ui/wash-module-sdk.js` | API helper (same-origin) |
| `ui/help.html` / `ui/help.ru.html` | Help (English / Russian) |
| `assets/icon.svg` | Catalog icon |
| `README.md` / `README.ru.md` | Documentation (English / Russian) |

## Environment variables

- `API_BASE_URL` — `http://dynamic-api:3001`
- `MODULE_DATA_DIR` — path to module `data/`
- `POLL_INTERVAL`, `GREETING` — from settingsSchema

## Publishing

1. Push to GitHub
2. Add an entry to [modules/registry.json](https://github.com/WASH-PRO/WASH-PRO-CRM/blob/main/modules/registry.json)
3. Dashboard → Modules → Refresh catalog → Install

Documentation: [WASH PRO CRM — Modules](https://wash-pro.github.io/WASH-PRO-CRM/en/modules/)
