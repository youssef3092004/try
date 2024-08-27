from flask import Blueprint, request, flash, redirect, url_for, render_template
from models.user import db, User
from models.cart import Cart
import uuid

cart = Blueprint('cart', __name__)

@cart.route('/cart', methods=['GET'])
def get_cart_items():
    cart_items = Cart.query.all()
    return render_template('cart.html', cart_items=cart_items)

@cart.route('/cart/<uuid:item_id>', methods=['GET'])
def get_cart_by_id(item_id):
    cart_item = Cart.query.get(item_id)
    if cart_item:
        return render_template('cart_item.html', cart_item=cart_item)
    else:
        flash('Item not found', category='error')
        return redirect(url_for('cart.get_cart_items'))

@cart.route('/cart/<uuid:item_id>/update', methods=['POST'])
def update_cart_item(item_id):
    data = request.form
    cart_item = Cart.query.get(item_id)
    if cart_item:
        if 'total_price' in data:
            cart_item.total_price = float(data['total_price'])
        if 'status' in data:
            cart_item.status = data['status']
        if 'user_id' in data:
            cart_item.user_id = int(data['user_id'])
        db.session.commit()
        flash('Item updated successfully', category='success')
        return redirect(url_for('cart.get_cart_by_id', item_id=item_id))
    else:
        flash('Item not found', category='error')
        return redirect(url_for('cart.get_cart_items'))

@cart.route('/cart/<uuid:item_id>/delete', methods=['POST'])
def remove_cart_item(item_id):
    cart_item = Cart.query.get(item_id)
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        flash('Item removed successfully', category='success')
        return '', 204  # No Content
    else:
        flash('Item not found', category='error')
        return '', 404  # Not Found

@cart.route('/cart/clear', methods=['POST'])
def remove_cart():
    cart_items = Cart.query.all()
    if cart_items:
        for item in cart_items:
            db.session.delete(item)
        db.session.commit()
        flash('Cart is now empty', category='success')
    else:
        flash('Cart is already empty', category='info')
    return redirect(url_for('cart.get_cart_items'))

@cart.route('/cart/create', methods=['POST'])
def create_item():
    data = request.form
    if not all(key in data for key in ('total_price', 'status', 'user_id')):
        flash('Invalid input data', category='error')
        return redirect(url_for('cart.get_cart_items'))
    user = User.query.get(data['user_id'])
    if not user:
        flash('User not found', category='error')
        return redirect(url_for('cart.get_cart_items'))
    new_cart = Cart(total_price=float(data['total_price']), status=data['status'], user_id=int(data['user_id']))
    db.session.add(new_cart)
    db.session.commit()
    flash('Item added to cart', category='success')
    return redirect(url_for('cart.get_cart_items'))
