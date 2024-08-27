from models import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from uuid import uuid4

class Book(db.Model):
    book_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    book_name = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    order_items = relationship('OrderItem', backref='book', lazy=True)

    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.author = author
        self.price = price

    def to_dict(self):
        return {
            'book_id': self.book_id,
            'book_name': self.book_name,
            'author': self.author,
            'price': self.price,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'order_items': [order_item.to_dict() for order_item in self.order_items]
        }
