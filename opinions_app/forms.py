from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional


class OpinionForm(FlaskForm):
    title = StringField(
        'Введите название фильма',
        validators=[DataRequired(message='Обязательное поле'), Length(1, 128)]
    )
    text = TextAreaField(
        'Напишите мнение',
        validators=[DataRequired(message='Обязательное поле')]
    )
    source = URLField(
        'Добавите ссылку на подробный обзор',
        validators=[Length(1, 256), Optional()]
    )
    submit = SubmitField('Добавить')

# для тестовой ветки