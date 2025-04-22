from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(50), nullable = False)
    is_active = db.Column(db.Boolean, nullable = False)

# class Heladería(db.Model):

#     id = db.Column(db.Integer, primary_key = True)
#     # más columnas

# class Producto(db.Model):
#     pass

# class Ingrediente(db.Model):
#     pass