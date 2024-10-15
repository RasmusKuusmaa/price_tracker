from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() 

user_products = db.Table('user_products',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    url = db.Column(db.String(500), nullable=False)
    original_price = db.Column(db.Float, nullable=True)
    last_price = db.Column(db.Float, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    products = db.relationship('Product', backref='user', lazy=True)