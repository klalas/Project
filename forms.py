from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo


class ContactForm(FlaskForm):
    vardas = StringField("Vardas", [DataRequired(), Length(min=5, message="per trumpa zinute")])
    pavadinimas = StringField('Tema', [DataRequired()])
    komentaras = TextAreaField('Tavo Komentaras', [DataRequired(), Length(min=20, message='per trumpa zinute')])

    submit = SubmitField('Komentuoti')

class SukurtiPica(FlaskForm):
    Company = StringField('Įmonė', [DataRequired()])
    Pizza_name = StringField('Picos pavadinimas', [DataRequired()])
    Ingredients= TextAreaField('Ingridientai')
    Price_S = StringField('Mažos picos kaina', [DataRequired()])
    Price_L = StringField('Didelės picos kaina', [DataRequired()])
    Img = StringField('Paveikslėlio nuoroda', [DataRequired()])
    submit = SubmitField('Siųsti')

class RegistracijosForma(FlaskForm):
    vardas= StringField('Vardas', [DataRequired()])
    el_pastas = StringField('El.paštas', [DataRequired()])
    slaptazodis = PasswordField('Slaptažodis', [DataRequired()])
    patvirtintas_slaptazodis= PasswordField('Pakartoti slaptažodį', [EqualTo('slaptazodis','slaptazodziai turi sutapti')])
    submit = SubmitField('Registruotis')

    def tikrinti_vartotoja(self, vardas):
        vartotojas= app.Vartotojas.query.filter_by(vardas=vardas.data).count() < 1
        if vartotojas:
            raise ValidationError ('sis vartotojas uzimtas')
    def tikrinti_pasta(self, el_pastas):
        vartotojas = app.Vartotojas.query.filter_by(el_pastas=el_pastas.data).first()
        if vartotojas:
            raise ValidationError ('sis pastas uzimtas')

class PrisijungimoForma(FlaskForm):
    el_pastas = StringField('el.pastas', [DataRequired()])
    slaptazodis = PasswordField('Slaptazodis', [DataRequired()])
    prisiminti= BooleanField('Prisiminti mane')
    submit = SubmitField('Prisijungti')

