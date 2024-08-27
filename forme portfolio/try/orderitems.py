from models import db
from uuid import uuid4

class OrderItem(db.Model):
    order_item_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    order_id = db.Column(db.String(36), db.ForeignKey('order.order_id'))
    book_id = db.Column(db.String(36), db.ForeignKey('book.book_id'))
    star_num = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def __init__(self, order_id, book_id, star_num, price):
        self.order_id = order_id
        self.book_id = book_id
        self.star_num = star_num
        self.price = price

    def to_dict(self):
        return {
            'order_item_id': self.order_item_id,
            'order_id': self.order_id,
            'book_id': self.book_id,
            'star_num': self.star_num,
            'price': self.price
        }
