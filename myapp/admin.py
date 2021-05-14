import re
from flask import Blueprint
from flask import render_template
from flask import flash
from flask import request
from flask import redirect
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from myapp.models import User, Role, News
from myapp import db
from flask_login import current_user, login_required
from sqlalchemy import insert, update, delete


admin = Blueprint('admin', __name__)


@admin.route('/')
@login_required
def dashboard():
    return redirect(url_for('admin.view_news'))

#---------------------------------------------------------

@admin.route('/admin/news')
@login_required
def view_news():
    news = News.query.all()
    return render_template('admin/news/admin_news.html', user=current_user, news=news)

@admin.route('/admin/news/create', methods=['GET', 'POST'])
@login_required
def create_news():
    if request.method == 'POST':
        title = request.form.get('title')
        message = request.form.get('message')
        file = request.form.get('file')

        if not title or not message:
            flash('Field canot be empty')
        else:
            new_news = News(news_title=title, news_message=message, news_file=file)
            db.session.add(new_news)
            db.session.commit()
            return redirect(url_for('admin.view_news'))
    return render_template('admin/news/create_news.html', user=current_user)

@admin.route('/<int:id>/admin/news/update', methods=['GET', 'POST'])
@login_required
def update_news(id):
    if request.method == 'POST':
        title = request.form.get('title')
        message = request.form.get('message')
        file = request.form.get('file')

        news = News.query.filter_by(id=id).first()
        news.news_title = title
        news.news_message = message
        news.news_file = file
        db.session.commit()
        return redirect(url_for('admin.view_news'))
    return render_template('admin/news/update_news.html', user=current_user)

@admin.route('/<int:id>/admin/news/delete', methods=['GET', 'POST'])
@login_required
def delete_news(id):
    news = News.query.filter_by(id=id).first()
    db.session.delete(news)
    db.session.commit()
    return redirect(url_for('admin.view_news'))

#---------------------------------------------------------

@admin.route('/admin/schedule')
@login_required
def view_schedule():
    return render_template('admin/admin_schedule.html', user=current_user)

#---------------------------------------------------------

@admin.route('/admin/subject')
@login_required
def view_subject():
    return render_template('admin/admin_subject.html', user=current_user)

#---------------------------------------------------------

@admin.route('/admin/user')
@login_required
def view_user():
    return render_template('admin/admin_user.html', user=current_user)

#---------------------------------------------------------