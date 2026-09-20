# Windows File Automator

**Автоматизация Windows: мониторинг, batch, Excel**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-Shamanchi-green)](LICENSE)

---

## Описание

Автоматизация файловых операций в Windows:
- Мониторинг папок через watchdog
- Batch-обработка файлов
- Генерация Excel-отчётов (openpyxl)
- SQLite для логирования

---

## Быстрый старт
`ash
git clone https://github.com/Shamanchi/windows-file-automator
cd windows-file-automator
cp .env.example .env
docker-compose up -d
`

### Переменные окружения
| Переменная | Описание |
|------------|----------|
| WATCH_PATHS | Пути для мониторинга (через запятую) |
| OUTPUT_PATH | Папка для результатов |
| EXCEL_TEMPLATE | Шаблон Excel |

---

## Тесты
`ash
pytest -v
`

---

## Docker
`ash
docker build -t windows-file-automator .
docker-compose up -d
`

---

## Структура
`
├── app/
│   ├── api/routes.py
│   ├── core/config.py
│   ├── core/logging.py
│   ├── services/watcher.py
│   └── main.py
├── tests/test_api.py
├── .github/workflows/ci.yml
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
`

---

## CI/CD
GitHub Actions: Ruff, MyPy, Pytest, Docker build

---

## Контакты

- Telegram: [@PavelYrevichh](https://t.me/PavelYrevichh)
- Email: [Lietman46@mail.ru](mailto:Lietman46@mail.ru)
- GitHub: [Shamanchi](https://github.com/Shamanchi)
- FL.ru: [Shamanchi](https://www.fl.ru/users/Shamanchi)

## Лицензия
Лицензия Shamanchi 1.0 (source-available) — см. [LICENSE](LICENSE).
---

> Источник темы: Каталог портфолио, запись windows-file-automator