# GTEC-ZAMENS

## Описание

Gtec-zamens веб-сервис для автоматического перевода расписание учебных занятий с world документа в нужный формат
расписания. Приложение предоставляет REST API для получения данных расписания в форматах YAML и JSON с возможностью фильтрации по группам.

## Возможности

- 📅 Получение полного расписания в форматах YAML и JSON
- 🔍 Фильтрация расписания по конкретным учебным группам
- 📊 Работа с несколькими версиями данных (базовая, результирующая, VIP)
- 🎯 Автоматическое сопоставление названий предметов с помощью нечеткого поиска
- ⚡ Асинхронная обработка запросов

## Структура проекта

```
├── main.py                           # Основной FastAPI сервер
├── mashed_test.py                    # Модуль нечеткого поиска предметов
├── test.py                          # Тестовый файл
├── testpars.py                      # Парсер данных
├── array.json                       # Массив соответствий предметов
├── array_test.json                  # Тестовый массив
├── version_output/                  # Директория с выходными данными
│   ├── output.yaml                  # Базовое расписание (YAML)
│   ├── output.json                  # Базовое расписание (JSON)
│   ├── output_result.yaml           # Результирующее расписание (YAML)
│   ├── output_result.json           # Результирующее расписание (JSON)
│   ├── output_result_mashed.yaml    # VIP расписание (YAML)
│   └── output_result_mashed.json    # VIP расписание (JSON)
└── temp/                           # Временные файлы
```

## Установка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd gtec_doc/new_version
```

2. Установите зависимости:
```bash
pip install fastapi uvicorn pyyaml requests rapidfuzz
```

## Запуск

Запустите сервер:
```bash
python main.py
```

Или используя uvicorn напрямую:
```bash
uvicorn main:app --reload
```

Сервер будет доступен по адресу: `http://localhost:8000`

## API Endpoints

### YAML Endpoints

- **GET** `/yaml_zamen` - Получить полное расписание в формате YAML
- **GET** `/yaml_zamen:{group_id}` - Получить расписание конкретной группы в формате YAML
- **GET** `/yaml_zamen.result` - Получить результирующее расписание в формате YAML
- **GET** `/yaml_zamen.result:{group_id}` - Получить результирующее расписание группы в формате YAML
- **GET** `/yaml_zamen.result.vip` - Получить VIP расписание в формате YAML

### JSON Endpoints

- **GET** `/json_zamen` - Получить полное расписание в формате JSON
- **GET** `/json_zamen:{group_id}` - Получить расписание конкретной группы в формате JSON
- **GET** `/json_zamen.result` - Получить результирующее расписание в формате JSON
- **GET** `/json_zamen.result:{group_id}` - Получить результирующее расписание группы в формате JSON
- **GET** `/json_zamen.result.vip` - Получить VIP расписание в формате JSON

## Примеры использования

### Получение полного расписания
```bash
curl http://localhost:8000/json_zamen
```

### Получение расписания конкретной группы
```bash
curl http://localhost:8000/yaml_zamen:Б-21
```

### Получение результирующего расписания
```bash
curl http://localhost:8000/json_zamen.result
```

## Формат данных

Расписание структурировано по группам и парам:

```yaml
data: 01.07.2025
Б-21:
  '1':
  - Физкультура Основы менеджмента
  - Финансы и кр Селицкая Т.В.
  '2':
  - Финансы и кр Селицкая Т.В.
  - Ин.яз проф лек Муринова В.В. Стасенко О.С.
```

## Технические детали

- **Framework**: FastAPI
- **Python**: 3.7+
- **Форматы данных**: YAML, JSON
- **Нечеткий поиск**: RapidFuzz
- **Асинхронность**: asyncio

## Особенности

- Автоматическая обработка ошибок при чтении файлов
- Поддержка Unicode (UTF-8)
- Нечеткое сопоставление названий предметов
- Валидация YAML и JSON данных
- Автоматическая документация API (Swagger UI доступен по `/docs`)

## Обработка ошибок

API возвращает соответствующие HTTP статусы:
- `404` - Файл не найден
- `400` - Ошибка парсинга YAML/JSON
- `200` - Успешный ответ

## Разработка

Для разработки рекомендуется использовать режим автоперезагрузки:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```


[![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=leshay)](https://github.com/anuraghazra/github-readme-stats)
