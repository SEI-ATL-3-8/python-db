from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    apartments = db.relationship('Apartment')


#Owners has many apartments(1-to-m)

class Apartment(db.Model):
    __tablename__ = 'apartments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    units = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))
    owner = db.relationship('Owner')


#Apartment belongs to Owner(1-to-m)
