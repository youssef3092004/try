from models import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from uuid import uuid4

class CartItem(db.Model):
    cart_item_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    cart_id = db.Column(db.String(36), db.ForeignKey('cart.cart_id'))
    book_id = db.Column(db.String(36), db.ForeignKey('book.book_id'))
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, cart_id, book_id, quantity):
        self.cart_id = cart_id
        self.book_id = book_id
        self.quantity = quantity

    def to_dict(self):
        return {
            'cart_item_id': self.cart_item_id,
            'cart_id': self.cart_id,
            'book_id': self.book_id,
            'quantity': self.quantity
        }
