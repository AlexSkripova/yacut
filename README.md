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

4. **Настройка переменных окружения:**
   
   Создайте файл `.env` в корне проекта:
   ```env
   FLASK_APP=yacut
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   DATABASE_URI=sqlite:///yacut.db
   ```

5. **Инициализация базы данных:**
   ```bash
   flask db upgrade
   ```

6. **Запуск приложения:**
   ```bash
   flask run
   ```

   Приложение будет доступно по адресу: http://localhost:5000
   ```

### Запуск тестов

```bash
pytest tests/ -v
```


##  API

### Базовый URL
```
http://localhost:5000/api
```

### Эндпоинты

#### POST /api/id/
Создание короткой ссылки

**Запрос:**
```json
{
  "url": "https://example.com/very/long/url",
  "custom_id": "short" // необязательный
}
```

**Ответ (201):**
```json
{
  "url": "https://example.com/very/long/url",
  "short_link": "http://localhost:5000/short"
}
```

**Ошибки:**
- `400` - Некорректные данные запроса
- `400` - Короткая ссылка уже существует

#### GET /api/id/{short_id}/
Получение оригинальной ссылки

**Ответ (200):**
```json
{
  "url": "https://example.com/very/long/url"
}
```

**Ошибки:**
- `404` - Указанный id не найден

### Ограничения

- **Максимальная длина custom_id:** 16 символов
- **Допустимые символы:** латинские буквы (a-Z) и цифры (0-9)
- **Автогенерируемый ID:** 6 случайных символов
- **Уникальность:** каждый короткий ID может использоваться только один раз

---

**Автор:** AlexSkripova  
**Репозиторий:** https://github.com/AlexSkripova/yacut