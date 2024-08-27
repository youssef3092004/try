from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import bcrypt
from uuid import uuid4

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.String(32), primary_key=True, default=lambda: uuid4().hex)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # one to many
    carts = db.relationship('Cart', back_populates='user')

    def __init__(self, fname, lname, username, email, password):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.email = email
        self.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def to_dict(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'carts': [cart.to_dict() for cart in self.carts]
        }
