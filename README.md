# 🔗 YaCut - URL Shortener Service

Сервис для укорачивания ссылок с веб-интерфейсом и REST API. Позволяет создавать короткие ссылки как автоматически, так и с пользовательскими идентификаторами.

## 📁 Структура проекта

```
yacut/
├── yacut/                      # Основной пакет приложения
│   ├── __init__.py            # Инициализация Flask приложения
│   ├── models.py              # Модели данных (URLMap)
│   ├── services.py            # Бизнес-логика (сервисный слой)
│   ├── forms.py               # WTForms для веб-интерфейса
│   ├── views.py               # Веб-контроллеры
│   ├── api_views.py           # API эндпоинты
│   ├── error_handlers.py      # Обработка ошибок
│   ├── utils.py               # Вспомогательные функции
│   ├── constants.py           # Константы приложения
│   ├── settings.py            # Конфигурация
│   ├── static/                # Статические файлы (CSS, JS, изображения)
│   └── templates/             # HTML шаблоны
├── migrations/                # Миграции базы данных
├── tests/                     # Тесты
├── requirements.txt           # Python зависимости
└── README.md                  # Документация
```

## 🚀 Установка и запуск

### Требования

- Python 3.7+
- pip
- Git

### Python зависимости:

```
Flask==3.0.2                  # Веб-фреймворк
Flask-SQLAlchemy==3.1.1       # ORM для работы с БД
Flask-Migrate==4.0.5          # Миграции БД
Flask-WTF==1.2.1              # Формы и CSRF защита
WTForms==3.0.1                # Валидация форм
SQLAlchemy==2.0.21            # ORM
python-dotenv==1.0.0          # Переменные окружения
```

### Локальная установка

1. **Клонирование репозитория:**
   ```bash
   git clone https://github.com/AlexSkripova/yacut.git
   cd yacut
   ```

2. **Создание виртуального окружения:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Установка зависимостей:**
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

### Примеры использования

**Создание ссылки с автоматическим ID:**
```bash
curl -X POST http://localhost:5000/api/id/ \
  -H "Content-Type: application/json" \
  -d '{"url": "https://github.com/AlexSkripova/yacut"}'
```

**Создание ссылки с пользовательским ID:**
```bash
curl -X POST http://localhost:5000/api/id/ \
  -H "Content-Type: application/json" \
  -d '{"url": "https://github.com/AlexSkripova/yacut", "custom_id": "github"}'
```

**Получение оригинальной ссылки:**
```bash
curl http://localhost:5000/api/id/github/
```

### Ограничения

- **Максимальная длина custom_id:** 16 символов
- **Допустимые символы:** латинские буквы (a-Z) и цифры (0-9)
- **Автогенерируемый ID:** 6 случайных символов
- **Уникальность:** каждый короткий ID может использоваться только один раз

---

**Автор:** AlexSkripova  
**Репозиторий:** https://github.com/AlexSkripova/yacut