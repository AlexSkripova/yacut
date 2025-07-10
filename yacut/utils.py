import random

from yacut.constants import (
    SHORT_ID_CHARACTERS, SHORT_ID_GENERATION_ATTEMPTS, SHORT_ID_LENGTH
)


def get_unique_short_id(length=SHORT_ID_LENGTH):
    """Генерирует уникальный короткий идентификатор для ссылки."""
    from yacut.services import URLMapService

    for attempt in range(SHORT_ID_GENERATION_ATTEMPTS):
        short_id = ''.join(random.choice(SHORT_ID_CHARACTERS)
                           for _ in range(length))
        if not URLMapService.is_short_id_exists(short_id):
            return short_id
    raise RuntimeError(
        'Не удалось сгенерировать уникальный короткий идентификатор'
        f'за {SHORT_ID_GENERATION_ATTEMPTS} попыток'
    )