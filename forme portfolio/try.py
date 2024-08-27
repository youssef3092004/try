# from flask import Blueprint, request, jsonify
# from models.user import db, User
# from models.cart import Cart


# cart = Blueprint('cart', __name__)


# #todo done
# @cart.route('/api/cart', methods=['GET'])
# def get_cart_items():
#     cart_items = Cart.query.all()
#     if cart_items:
#         return jsonify({'cart_items': [cart.to_dict() for cart in cart_items]}), 200
#     else:
#         return jsonify({'message': 'No items in cart'}), 404

# #todo done
# @cart.route('/api/cart/<int:item_id>', methods=['GET'])
# def get_cart_by_id(item_id):
#     cart_items = Cart.query.get(item_id)
#     if cart_items:
#         return jsonify(cart_items.to_dict())
#     else:
#         return jsonify({'message': 'Item not found'}), 404

# #todo done
# @cart.route('/api/cart/<int:item_id>', methods=['PUT'])
# def update_cart_item(item_id):
#     data = request.get_json()
#     cart_items = Cart.query.get(item_id)
#     if data:
#         for item in cart_items:
#             if item.get('id') == item_id:
#                 if 'name' in data:
#                     item['name'] = data['name']
#                 if 'quantity' in data:
#                     item['quantity'] = data['quantity']
#                 if 'price' in data:
#                     item['price'] = data['price']
#                 return jsonify(item.to_dict()), 200
#         return jsonify({'message': 'Item not found'}), 404
#     else:
#         return jsonify({'message': 'No input data provided'}), 400

# #todo done
# @cart.route('/api/cart/<int:item_id>', methods=['DELETE'])
# def remove_cart_item(item_id):
#     cart_items = Cart.query.get(item_id)
#     if cart_items:
#         db.session.delete(cart_items)
#         db.session.commit()
#         return jsonify({'message': 'Item removed'}), 200
#     else:
#         return jsonify({'message': 'Item not found'}), 404

# #todo done
# @cart.route('/api/cart', methods=['DELETE'])
# def remove_cart():
#     cart_items = Cart.query.all()
#     if cart_items:
#         db.session.delete(cart_items)
#         db.session.commit()
#         return jsonify({'message': 'Cart is empty now'}), 200
#     else:
#         return jsonify({'message': 'Cart is already empty'}), 404

# #todo done
# @cart.route('/api/cart/create', methods=['POST'])
# def create_item():
#     data = request.get_json()
#     if not data or not all(key in data for key in ('total_price', 'status', 'user_id')):
#         return jsonify({'message': 'Invalid input data'}), 400
#     user = User.query.get(data['user_id'])
#     if not user:
#         return jsonify({'message': 'User not found'}), 404
#     new_cart = Cart(total_price=data['total_price'], status=data['status'], user_id=data['user_id'])
#     db.session.add(new_cart)
#     db.session.commit()
#     return jsonify({'message': 'Item added', 'item': new_cart.to_dict()}), 201
