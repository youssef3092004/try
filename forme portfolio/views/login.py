from flask import Blueprint, request, flash, redirect, url_for, render_template, session
from models.user import User

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST', 'GET'])
def login_view():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            flash('All fields are required', category='error')
            return redirect(url_for('login.login_view'))
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['email'] = user.email
            flash('Login successful!', category='success')
            return redirect(url_for('dashboard.dashboard_view'))
        else:
            flash('Invalid email or password', category='error')
            return redirect(url_for('login.login_view'))
    return render_template('login.html')
