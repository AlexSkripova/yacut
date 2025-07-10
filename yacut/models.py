from datetime import datetime

from yacut import db


class URLMap(db.Model):
    """Модель для хранения соответствий между длинными и короткими ссылками."""

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
