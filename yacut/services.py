import random
import re

from yacut import db
from yacut.constants import (
    SHORT_ID_CHARACTERS, SHORT_ID_LENGTH, SHORT_ID_MAX_LENGTH, SHORT_ID_PATTERN
)
from yacut.models import URLMap


class URLMapService:
    """Сервисный класс для работы с URLMap."""

    @staticmethod
    def validate_custom_id(custom_id):
        """Валидация custom_id. Генерирует ValueError при ошибке."""
        if not re.match(SHORT_ID_PATTERN, custom_id):
            raise ValueError('Указано недопустимое имя для короткой ссылки')

        if len(custom_id) > SHORT_ID_MAX_LENGTH:
            raise ValueError('Указано недопустимое имя для короткой ссылки')

    @staticmethod
    def is_short_id_exists(short_id):
        """Проверка существования короткого идентификатора."""
        return URLMap.query.filter_by(short=short_id).first() is not None

    @staticmethod
    def get_by_short_id(short_id):
        """Получение URLMap по короткому идентификатору."""
        return URLMap.query.filter_by(short=short_id).first()

    @staticmethod
    def get_unique_short_id(length=SHORT_ID_LENGTH):
        """Генерирует уникальный короткий идентификатор для ссылки."""
        short_id = ''.join(random.choices(SHORT_ID_CHARACTERS, k=length))
        if URLMapService.is_short_id_exists(short_id):
            raise RuntimeError(
                'Не удалось сгенерировать уникальный короткий идентификатор'
            )
        return short_id

    @staticmethod
    def create_url_map(original_url, custom_id=None):
        """Создание URLMap с валидацией и проверкой уникальности."""
        if custom_id:
            URLMapService.validate_custom_id(custom_id)

            if URLMapService.is_short_id_exists(custom_id):
                raise ValueError(
                    'Предложенный вариант короткой ссылки уже существует.'
                )

            short_id = custom_id
        else:
            short_id = URLMapService.get_unique_short_id()

        url_map = URLMap(
            original=original_url,
            short=short_id
        )
        db.session.add(url_map)
        db.session.commit()

        return url_map