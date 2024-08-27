from models import db
from sqlalchemy.orm import relationship
from uuid import uuid4

class Category(db.Model):
    category_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500))
    books = relationship('Book', backref='category', lazy=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            'category_id': self.category_id,
            'name': self.name,
            'description': self.description,
            'books': [book.to_dict() for book in self.books]
        }
