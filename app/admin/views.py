
from werkzeug.security import check_password_hash
from app.models.User import User
from flask import render_template, request
from jinja2  import TemplateNotFound
from flask.helpers import flash, url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from datetime import datetime
from datetime import timedelta
from . import admin
from .. import db


@admin.route('/dashboard')
@login_required
def dashboard():
    return render_template('admin/dashboard.html', title="Dashboard")

@admin.route('/profile')
@login_required
def profile():
    """
    Render the profile page template on the / route
    """
    try:
        if current_user.is_authenticated:
            user = current_user  
                    
        return render_template('admin/profile.html', title="Profile Management", page_header_title = 'User Profile')
    except TemplateNotFound:
        return render_template('includes/404.html'), 404
    
@admin.route('/profile-update/<int:user_id>', methods=["POST"])
@login_required
def profile_update(user_id):
    if request.method == 'POST':
        user = User.query.get(user_id)  
        user.name = request.form['name']
        user.user_name = request.form['user_name']
        user.phone = request.form['phone']
        user.address = request.form['address']

        db.session.commit()
        flash("Profile updated successfully !!", "success")
                    
        return redirect(url_for('.profile'))

@admin.route('/change-password', methods=["POST"])
@login_required
def change_password():
    if request.method == 'POST':
        old_password = request.form['old_password']
        current_password = current_user.password_hash
        new_password = request.form['password']
        if check_password_hash(current_password,old_password):
            user = User.query.get(current_user.id)
            user.password = new_password
            db.session.commit()
            flash("Password Updated successfully", "success")
        else:
            flash("Invalid Password or old password doesn't match", "error") 
               
        return redirect(url_for('.profile'))
