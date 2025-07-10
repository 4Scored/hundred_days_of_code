import os
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("APP_SECRET_KEY")
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id) # User.get(user_id)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(UserMixin, db.Model): # Mixin
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

with app.app_context():
    db.create_all()

# routes/functions
@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        hashedword = generate_password_hash(request.form.get("password"), "pbkdf2:sha256", 8)
        user_to_register = User(
            name = request.form.get("name"),
            email = request.form.get("email"),
            password = hashedword,
        )
        user = db.session.execute(db.select(User).where(User.email == user_to_register.email)).scalar()
        if user: # exists already
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        else: # sign them up
            db.session.add(user_to_register)            
            db.session.commit()            
            login_user(user_to_register)
            return redirect(url_for('secrets')) # return render_template("secrets.html", name=user_to_register.name)
    return render_template("register.html", logged_in=current_user.is_authenticated)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = db.session.execute(db.select(User).where(User.email == email)).scalar() # password checked below, no need here
        if not user: # user doesn't exist
            flash("That email does not exist, please try again.")
        elif not check_password_hash(user.password, password): # incorrect password
            flash('Password incorrect, please try again.')            
        else: # user exists
            login_user(user)
            return redirect(url_for('secrets'))
        return redirect(url_for('login'))
    return render_template("login.html", logged_in=current_user.is_authenticated)

@app.route('/secrets')
@login_required
def secrets():    
    return render_template("secrets.html", name=current_user.name, logged_in=True)

@app.route('/logout')
# @login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download', methods=["GET", "POST"])
@login_required
def download():
    return send_from_directory("static", path="files/cheat_sheet.pdf")

if __name__ == "__main__":
    app.run(debug=True)
