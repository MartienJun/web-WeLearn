from flask import Blueprint
from flask import render_template
from flask import flash
from flask import request
from flask import redirect
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from myapp.models import User, Role
from myapp import db
from flask_login import current_user, login_required


admin = Blueprint('admin', __name__)


@admin.route('/')
@login_required
def dashboard():
    return redirect(url_for('admin.view_news'))

#---------------------------------------------------------

@admin.route('/admin/news')
def view_news():
    return render_template('admin/admin_news.html')

#---------------------------------------------------------

@admin.route('/admin/schedule')
def view_schedule():
    return render_template('admin/admin_schedule.html')

#---------------------------------------------------------

@admin.route('/admin/subject')
def view_subject():
    return render_template('admin/admin_subject.html')

#---------------------------------------------------------

@admin.route('/admin/user')
def view_user():
    return render_template('admin/admin_user.html')

#---------------------------------------------------------