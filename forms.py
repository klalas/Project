from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo


class ContactForm(FlaskForm):
    name = StringField("Vardas", [DataRequired(), Length(min=5, message="per trumpa zinute")])
    email = StringField('el.pastas', [Email(message="Neteisingas adresas."), DataRequired()])
    body = TextAreaField('jusu pranesimas', [DataRequired(), Length(min=20, message='per trumoa zinute')])

    submit = SubmitField('Siusti')

class RegistracijosForma(FlaskForm):
    vardas= StringField('Vardas', [DataRequired()])
    el_pastas = StringField('el.pastas', [DataRequired()])
    slaptazodis = PasswordField('Slaptazodis', [DataRequired()])
    patvirtintas_slaptazodis= PasswordField('Pakartoti slaptazodi', [EqualTo('slaptazodis','slaptazodziai turi sutapti')])
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

class rasytiStraipsni(FlaskForm):
    autorius = StringField('Vardas Pavarde', [DataRequired()])
    pavadinimas = StringField('Pavadinimas', [DataRequired(), Length(min=50, message='per trumpas straipsnis')])
    straipsnis= TextAreaField('Ivesti teksta')
    submit = SubmitField('Siusti')