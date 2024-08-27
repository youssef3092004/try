from models import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from uuid import uuid4

class Cart(db.Model):
    cart_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    cart_items = relationship('CartItem', backref='cart', lazy=True)

    def __init__(self, user_id):
        self.user_id = user_id

    def to_dict(self):
        return {
            'cart_id': self.cart_id,
            'user_id': self.user_id,
            'created_at': self.created_at,
            'cart_items': [cart_item.to_dict() for cart_item in self.cart_items]
        }
