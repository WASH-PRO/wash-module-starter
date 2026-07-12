**Язык:** [English](README.md) · **Русский**

# wash-module-starter

Шаблон модуля WASH PRO CRM для разработки собственных расширений.

## Быстрый старт

```bash
git clone https://github.com/WASH-PRO/wash-module-starter my-wash-module
cd my-wash-module
# 1. Измените id/name в wash-module.json
# 2. Реализуйте логику в src/main.py
# 3. Настройте ui/index.html
```

## Файлы

| Файл | Назначение |
|------|------------|
| `wash-module.json` | Манифест для каталога CRM |
| `src/main.py` | Daemon (PyOrchestrator) |
| `ui/index.html` | Страница настроек (iframe в Dashboard) |
| `ui/wash-module-sdk.js` | API helper (same-origin) |
| `ui/help.html` / `ui/help.ru.html` | Справка (English / русский) |
| `assets/icon.svg` | Иконка в каталоге |
| `README.md` / `README.ru.md` | Документация (English / русский) |

## Переменные окружения

- `API_BASE_URL` — `http://dynamic-api:3001`
- `MODULE_DATA_DIR` — путь к `data/` модуля
- `POLL_INTERVAL`, `GREETING` — из settingsSchema

## Публикация

1. Push в GitHub
2. Добавьте запись в [modules/registry.json](https://github.com/WASH-PRO/WASH-PRO-CRM/blob/main/modules/registry.json)
3. Dashboard → Модули → Обновить каталог → Установить

Документация: [WASH PRO CRM — Модули](https://wash-pro.github.io/WASH-PRO-CRM/ru/modules/)
