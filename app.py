from flask import Flask,request, render_template, redirect,flash, url_for
from flask_sqlalchemy import SQLAlchemy
from dictionary import pizzas, kom, pizzasPicaPica, pizzasČilas, pizzasBrooklynBrothers
from datetime import date
from forms import ContactForm
from flask_login import LoginManager, UserMixin, current_user, logout_user, login_user, login_required
from forms import ContactForm, RegistracijosForma, PrisijungimoForma, SukurtiPica
from flask_bcrypt import Bcrypt
import os

app= Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'MLXH243GssUWwKdTWS7FDhdwYF56wPj8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'puslapiui.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

bcrypt= Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'registruotis'
login_manager.login_message_category= 'info'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html',  data=pizzas)

class Vartotojas(db.Model, UserMixin):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    vardas= db.Column("vardas", db.String(20), unique=True, nullable=False)
    el_pastas= db.Column("el_pastas", db.String(120), unique=False, nullable=False)
    slaptazodis= db.Column("slaptazodis", db.String(60), unique=True, nullable=False)



@login_manager.user_loader
def load_user(vartotojo_id):
    return Vartotojas.query.get(int(vartotojo_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistracijosForma()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.slaptazodis.data).decode('utf-8')
        vartotojas= Vartotojas(vardas=form.vardas.data, el_pastas=form.el_pastas.data, slaptazodis=hashed_pwd)
        db.session.add(vartotojas)
        db.session.commit()
        flash("sekmingai prisiregistravote. galite prisijungti", 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title= 'Register', form=form)



@app.route('/komentarai', methods=['GET', 'POST'])
def komentarai():
    db.create_all()
    form = ContactForm()
    if form.validate_on_submit():
        komentaras= Komentaras(vardas=form.vardas.data, pavadinimas=form.pavadinimas.data, komentaras=form.komentaras.data)
        db.session.add(komentaras)
        db.session.commit()
        return render_template('contact_success.html', form=form)
    return render_template('komentarai.html', form=form, data=kom)

class Komentaras(db.Model):
    __tablename__='komentarai'
    id = db.Column(db.Integer, primary_key=True)
    vardas= db.Column("Vardas", db.String(30), unique=False, nullable=False)
    pavadinimas= db.Column("Pavadinimas", db.String(30), unique=True, nullable=False)
    komentaras= db.Column("Komentaras", db.String(200), unique=True, nullable=False)

@app.route('/nauja_pica', methods=['GET','POST'])
@login_required
def nauja_pica():
    db.create_all()
    form = SukurtiPica()
    if form.validate_on_submit():
        naujapica= NaujaPica(Company=form.Company.data, Pizza_name=form.Pizza_name.data, Ingredients=form.Ingredients.data, Price_S=form.Price_S.data, Price_L=form.Price_L.data, Img=form.Img.data)
        db.session.add(naujapica)
        db.session.commit()
        flash("Sekmingai sukurete nauja pica.", 'success')
        return redirect(url_for('index'))
    return render_template("nauja_pica.html", form=form)

class NaujaPica(db.Model):
    __tablename__='picos_csv'
    Company= db.Column("Company", db.String(30), primary_key=True)
    Pizza_name= db.Column("Pizza_name", db.String(30), unique=True, nullable=False)
    Ingredients= db.Column("Ingredients", db.String(200), unique=True, nullable=False)
    Price_S = db.Column("Price S", db.String(30), unique=True, nullable=False)
    Price_L = db.Column("Price L", db.String(30), unique=True, nullable=False)
    Img = db.Column("Img", db.String(80), unique=True, nullable=False)

@app.route('/login', methods= ['GET', 'POST'])
def login():
    form = PrisijungimoForma()
    if form.validate_on_submit():
        vartotojas = Vartotojas.query.filter_by(el_pastas=form.el_pastas.data).first()
        if vartotojas and bcrypt.check_password_hash(vartotojas.slaptazodis, form.slaptazodis.data):
            login_user(vartotojas, remember=form.prisiminti.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('prisijungimas nepavyko, patikrinkite varda el pasto', 'danger')
    return render_template('login.html', form=form, title='prisijungti')

@app.route('/picerijos', methods= ['GET','POST'])
def account():
    return render_template('picerijos.html')

@app.route('/PicaPica', methods= ['GET','POST'])
def PicaPica():
    return render_template('PicaPica.html', data=pizzasPicaPica)

@app.route('/BrooklynBrothers', methods= ['GET','POST'])
def BrooklynBrothers():
    return render_template('BrooklynBrothers.html', data=pizzasBrooklynBrothers)

@app.route('/Čilas', methods= ['GET','POST'])
def Čilas():
    return render_template('Čilas.html', data=pizzasČilas)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/add_article')
def article():
   return render_template('single_article.html', data=data)





@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)