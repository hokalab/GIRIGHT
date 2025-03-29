from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Optional

class GearForm(FlaskForm):
    name = StringField('ギア名', validators=[DataRequired()])
    manufacturer = StringField('メーカー', validators=[Optional()])
    weight = FloatField('重さ（g）', validators=[DataRequired()])
    category = SelectField('カテゴリ', choices=[
        ('shelter', 'Shelter'),
        ('sleep', 'Sleep'),
        ('pack', 'Pack'),
        ('cook', 'Cook'),
        ('wear', 'Wear'),
        ('water', 'Water'),
        ('elec', 'Electronics'),
        ('misc', 'Misc')
    ])
    essential = BooleanField('必携ギア？')
    is_packed = BooleanField('今回持ってく')  # ← これ追加！
    notes = TextAreaField('メモ')
    submit = SubmitField('登録')