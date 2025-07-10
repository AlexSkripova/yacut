from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from yacut.constants import SHORT_ID_MAX_LENGTH, SHORT_ID_PATTERN


class URLForm(FlaskForm):
    """Форма для создания коротких ссылок."""

    original_link = StringField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Поле обязательно для заполнения'),
            URL(message='Некорректный URL')
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(
                max=SHORT_ID_MAX_LENGTH,
                message='Максимальная длина идентификатора —'
                        f'{SHORT_ID_MAX_LENGTH} символов'
            ),
            Regexp(
                SHORT_ID_PATTERN,
                message='Идентификатор может содержать'
                        'только латинские буквы и цифры'
            )
        ]
    )
    submit = SubmitField('Создать')
