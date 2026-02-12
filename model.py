from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)
    wallet = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<User {self.phone}>"



class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_phone = db.Column(db.String(20))
    crop_name = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    location = db.Column(db.String(200))
    status = db.Column(db.String(50), default="Available")



class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buyer_phone = db.Column(db.String(20))
    farmer_phone = db.Column(db.String(20))
    crop_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    total_price = db.Column(db.Integer)
    status = db.Column(db.String(50), default="Pending")