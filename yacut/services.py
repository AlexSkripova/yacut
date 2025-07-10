import re

from yacut import db
from yacut.constants import SHORT_ID_MAX_LENGTH, SHORT_ID_PATTERN
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


class URLMapService:
    """Сервисный класс для работы с URLMap."""

    @staticmethod
    def validate_custom_id(custom_id):
        """Валидация custom_id. Возвращает ошибку или None."""
        if not re.match(SHORT_ID_PATTERN, custom_id):
            return 'Указано недопустимое имя для короткой ссылки'

        if len(custom_id) > SHORT_ID_MAX_LENGTH:
            return 'Указано недопустимое имя для короткой ссылки'

        return None

    @staticmethod
    def is_short_id_exists(short_id):
        """Проверка существования короткого идентификатора."""
        return URLMap.query.filter_by(short=short_id).first() is not None

    @staticmethod
    def get_by_short_id(short_id):
        """Получение URLMap по короткому идентификатору."""
        return URLMap.query.filter_by(short=short_id).first()

    @staticmethod
    def create_url_map(original_url, custom_id=None):
        """Создание URLMap с валидацией и проверкой уникальности."""
        if custom_id:
            validation_error = URLMapService.validate_custom_id(custom_id)
            if validation_error:
                raise ValueError(validation_error)

            if URLMapService.is_short_id_exists(custom_id):
                raise ValueError(
                    'Предложенный вариант короткой ссылки уже существует.'
                )

            short_id = custom_id
        else:
            short_id = get_unique_short_id()

        url_map = URLMap(
            original=original_url,
            short=short_id
        )
        db.session.add(url_map)
        db.session.commit()

        return url_map