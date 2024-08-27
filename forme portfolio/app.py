from flask import Flask, jsonify
from models.user import db, User
from models.cart import Cart
from flask_cors import CORS
from views.login import login as login_blueprint
from views.register import register as register_blueprint
from views.logout import logout as logout_blueprint
from views.dashboard import dashboard as dashboard_blueprint
from views.home import home as home_blueprint
from views.cart import cart as cart_blueprint
import random
from werkzeug.security import generate_password_hash

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

app.register_blueprint(login_blueprint, url_prefix='/')
app.register_blueprint(register_blueprint, url_prefix='/')
app.register_blueprint(logout_blueprint, url_prefix='/')
app.register_blueprint(dashboard_blueprint, url_prefix='/')
app.register_blueprint(home_blueprint, url_prefix='/')
app.register_blueprint(cart_blueprint, url_prefix='/api')

with app.app_context():
    db.create_all()

@app.route('/insert_dummy_users', methods=['GET'])
def insert_dummy_users():
    try:
        # Insert 5 dummy users
        for i in range(5):
            password_hash = generate_password_hash('123', method='pbkdf2:sha256')  # Corrected hashing method
            new_user = User(
                username=f'user_{i+1}',  # Example username
                email=f'user_{i+1}@example.com',  # Example email
                password=password_hash  # Example hashed password
                # Add other fields as needed
            )
            db.session.add(new_user)
        
        db.session.commit()
        return jsonify({"message": "5 dummy users inserted successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/insert_dummy_carts', methods=['GET'])
def insert_dummy_carts():
    try:
        # Fetch users to associate with the carts
        users = User.query.all()
        if not users:
            return jsonify({"error": "No users found in the database"}), 404
        
        # Insert 20 dummy cart items
        for _ in range(20):
            user = random.choice(users)  # Randomly select a user
            new_cart = Cart(
                total_price=random.uniform(10.0, 100.0),  # Random price between 10.0 and 100.0
                status=random.choice(['active', 'inactive']),  # Random status
                user_id=user.id  # Associate with a random user
            )
            db.session.add(new_cart)
        
        db.session.commit()
        return jsonify({"message": "20 dummy cart items inserted successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
