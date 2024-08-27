from models import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from uuid import uuid4

class Order(db.Model):
    order_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'))
    order_date = db.Column(db.DateTime(timezone=True), default=func.now())
    total_amount = db.Column(db.Integer)
    order_items = relationship('OrderItem', backref='order', lazy=True)

    def __init__(self, user_id, total_amount):
        self.user_id = user_id
        self.total_amount = total_amount

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'order_date': self.order_date,
            'total_amount': self.total_amount,
            'order_items': [order_item.to_dict() for order_item in self.order_items]
        }
