# Scrapy Parser PEP

Парсер для извлечения информации о Python Enhancement Proposals (PEP) с официального сайта https://peps.python.org/

## Описание

Проект представляет собой веб-скрейпер, построенный на фреймворке Scrapy, который автоматически собирает данные обо всех PEP документах и создает два отчета:

1. **Полный список PEP** - CSV файл со всеми документами (номер, название, статус)
2. **Сводка по статусам** - CSV файл с подсчетом количества документов в каждом статусе

## Структура проекта

```
scrapy_parser_pep/
├── pep_parse/
│   ├── spiders/
│   │   └── pep.py          # Spider для парсинга PEP
│   ├── items.py            # Определение структуры данных
│   ├── pipelines.py        # Обработка и сохранение данных
│   └── settings.py         # Настройки Scrapy
├── results/                # Директория с результатами
├── tests/                  # Тесты
├── requirements.txt        # Зависимости
└── scrapy.cfg             # Конфигурация Scrapy
```

## Установка и запуск

### 1. Клонирование репозитория
```bash
git clone git@github.com:AlexSkripova/scrapy_parser_pep.git
cd scrapy_parser_pep
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Запуск парсера
```bash
scrapy crawl pep
```

## Результаты работы

После запуска в директории `results/` создаются два файла:

### 1. Список PEP (`pep_ДАТА-ВРЕМЯ.csv`)
```csv
number,name,status
1,PEP Purpose and Guidelines,Active
8,Style Guide for Python Code,Active
20,The Zen of Python,Active
```

### 2. Сводка по статусам (`status_summary_ДАТА-ВРЕМЯ.csv`)
```csv
Статус,Количество
Final,285
Active,55
Draft,23
Total,363
```

## Архитектура

### Spider (`pep.py`)
- `parse()` - собирает ссылки на все PEP документы с главной страницы
- `parse_pep()` - извлекает данные из каждого документа (номер, название, статус)

### Items (`items.py`)
- `PepParseItem` - структура данных с полями: `number`, `name`, `status`

### Pipeline (`pipelines.py`)
- `PepParsePipeline` - обрабатывает Items, подсчитывает статусы, создает сводку

### Настройки (`settings.py`)
- Конфигурация Feeds для сохранения основного CSV
- Настройки Pipeline для обработки данных

## Требования

- Python 3.7+
- Scrapy 2.5.1
- pytest 6.2.5
- Другие зависимости указаны в `requirements.txt`


### Автор: Александра Скрипова