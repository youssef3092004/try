from flask import Blueprint, session, flash, redirect, url_for

logout = Blueprint('logout', __name__)

@logout.route('/logout', methods=['POST', 'GET'])
def logout_view():
    if 'email' in session:
        session.pop('email', None)
        flash('Logout successful')
        return redirect(url_for('login.login_view'))
    else:
        flash('You are not logged in')
        return redirect(url_for('login.login_view'))
