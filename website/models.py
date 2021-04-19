from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date_time = db.Column(db.DateTime(timezone = True),default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, data, date_time):
        self.data = data
        self.date_time = date_time

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150),unique = True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    age = db.Column(db.Integer)
    profession = db.Column(db.String(150))
    password = db.Column(db.String(150))
    notes = db.relationship('Note')

    def __init__(self, email, first_name, last_name, gender, age, profession,password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.profession = profession
        self.password = password

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150))
    author_name = db.Column(db.String(150))
    publication = db.Column(db.String(150))
    purchase_date = db.Column(db.DateTime(timezone = True),default = func.now())
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    available_quantity = db.Column(db.Integer)

    def __init__(self, name, author_name, publication, purchase_date, price, quantity, available_quantity):
        self.name = name
        self.author_name = author_name
        self.publication = publication
        self.purchase_date = purchase_date
        self.price = price
        self.quantity = quantity
        self.available_quantity = available_quantity

class Member(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150),unique = True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    age = db.Column(db.Integer)
    profession = db.Column(db.String(150))

    def __init__(self, email, first_name, last_name, gender, age, profession):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.profession = profession
