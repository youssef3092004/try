from flask import Blueprint, render_template, session
from models.user import User

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard', methods=['GET'])
def dashboard_view():
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html', user=user)
    else:
        return render_template('login.html')
