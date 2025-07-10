from datetime import datetime

from yacut import db
from yacut.constants import SHORT_FIELD_MAX_LENGTH


class URLMap(db.Model):
    """Модель для хранения соответствий между длинными и короткими ссылками."""

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(SHORT_FIELD_MAX_LENGTH),
                      unique=True, nullable=False, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
