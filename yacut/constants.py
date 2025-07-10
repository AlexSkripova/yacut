import string

# Константы для коротких идентификаторов
SHORT_ID_LENGTH = 6
SHORT_ID_MAX_LENGTH = 16
SHORT_ID_CHARACTERS = string.ascii_letters + string.digits
SHORT_ID_GENERATION_ATTEMPTS = 1000

# Регулярные выражения
SHORT_ID_PATTERN = r'^[a-zA-Z0-9]+$'

# Константы для полей базы данных
SHORT_FIELD_MAX_LENGTH = 16