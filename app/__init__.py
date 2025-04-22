from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from app.config.auth import login_manager
from app.config.db import db, User

def create_app(config):

    app = Flask(__name__, template_folder = 'views')

    app.config.from_object(config)

    login_manager.init_app(app)
    db.init_app(app)

    @login_manager.user_loader
    def load_user(user_id:str) -> User:
        user = User.query.get(str(user_id))
        return user

    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/login', methods = ['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            print(username)
            print(password)
            # recuperamos el usuario de la bd
            usuario = User.query.filter_by(username = username, password = password).first()
            print(usuario.id)
            print(usuario.is_active)
            if usuario:
                return redirect(
                    url_for('dashboard')
                )
    @app.route('/dashboard', methods = ['GET', 'POST'])
    def dashboard():
        if request.method == 'GET':
            return render_template('dashboard.html')
        if request.method == 'POST':
            return redirect(
                url_for('logout')
            )
    
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(
            url_for('login')
        )
    
    with app.app_context():
        db.create_all()

    return app