from flask import Blueprint
from flask.templating import render_template


admin = Blueprint('admin', __name__)


@admin.route('/admin/dashboard')
def view_news():
    return render_template('admin/admin_news.html')


@admin.route('/admin/schedule')
def view_schedule():
    return render_template('admin/admin_schedule.html')


@admin.route('/admin/subject')
def view_subject():
    return render_template('admin/admin_subject.html')


@admin.route('/admin/user')
def view_user():
    return render_template('admin/admin_user.html')