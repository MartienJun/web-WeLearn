import os
from myapp import db, files
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from myapp.models import Schedule, User, News, Subject, Profile_Employee, Class


teacher = Blueprint('teacher', __name__)


@teacher.route('/')
@login_required
def teacher_dashboard():
    return redirect(url_for('teacher.view_news'))

#---------------------------------------------------------

@teacher.route('/teacher/news')
@login_required
def view_news():
    news = News.query.all()
    return render_template('teacher/news/teacher_news.html', news=news)