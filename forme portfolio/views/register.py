from flask import Blueprint, request, flash, redirect, url_for, render_template
from models.user import db, User

register = Blueprint('register', __name__)

@register.route('/register', methods=['POST', 'GET'])
def register_view():
    if request.method == 'POST':
        data = request.form
        fname = data.get('fname')
        lname = data.get('lname')
        username = data.get('username')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')
        if not fname or not lname or not username or not email or not password1 or not password2:
            flash('All fields are required', category='error')
            return redirect(url_for('register.register_view'))
        if User.query.filter_by(username=username).first():
            flash('Username already taken', category='error')
            return redirect(url_for('register.register_view'))
        if User.query.filter_by(email=email).first():
            flash('Email already registered', category='error')
            return redirect(url_for('register.register_view'))
        if password1 != password2:
            flash('Passwords do not match', category='error')
            return redirect(url_for('register.register_view'))
        new_user = User(fname=fname, lname=lname, username=username, email=email, password=password1)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', category='success')
        return redirect(url_for('login.login_view'))
    return render_template('register.html')
