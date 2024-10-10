from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() 

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    url = db.Column(db.String(500), nullable=False)
    original_price = db.Column(db.Float, nullable=True)
    cur_price = db.Column(db.Float, nullable=True)
    email = db.Column(db.String(100), nullable=False)
