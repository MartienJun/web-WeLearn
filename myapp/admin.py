import os
from flask import Blueprint, render_template, flash, redirect, url_for, request
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from myapp.models import User, Role, News, Subject
from myapp import db, files
from flask_login import current_user, login_required


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
    return render_template('admin/news/admin_news.html', this_user=current_user, news=news)


@admin.route('/admin/news/create', methods=['GET', 'POST'])
@login_required
def create_news():
    if request.method == 'POST':
        title = request.form.get('title')
        message = request.form.get('message')
        file = request.files['file']

        if not title or not message:
            flash('Field canot be empty')
        else:
            new_news = News(news_title=title, news_message=message, news_file=file.filename)
            db.session.add(new_news)
            db.session.commit()
            
            if file.filename != "":
                files.save(file)

            return redirect(url_for('admin.view_news'))
    return render_template('admin/news/create_news.html', this_user=current_user)


@admin.route('/<int:id>/admin/news/update', methods=['GET', 'POST'])
@login_required
def update_news(id):
    if request.method == 'POST':
        title = request.form.get('title')
        message = request.form.get('message')
        file = request.files['file']

        if not title or not message:
            flash('Field canot be empty')
        else:
            news = News.query.filter_by(id=id).first()
            news.news_title = title
            news.news_message = message
            news.news_file = file.filename
            db.session.commit()

            if file.filename != "":
                files.save(file)

            return redirect(url_for('admin.view_news'))
    return render_template('admin/news/update_news.html', this_user=current_user, news=News.query.filter_by(id=id).first())


@admin.route('/<int:id>/admin/news/delete', methods=['GET', 'POST'])
@login_required
def delete_news(id):
    news = News.query.filter_by(id=id).first()
    db.session.delete(news)
    db.session.commit()

    upload_file_path = os.path.join(os.path.join(os.path.realpath('.'), 'uploads'), news.news_file)
    print(upload_file_path)

    if os.path.exists(upload_file_path):
        print('ada')
    # if news.news_file != "":
    #     upload_file_path = os.path.join(os.path.realpath('.'), 'uploads')
    #     print(upload_file_path)
    #     #os.remove(os.path.join(upload_file_path, news.news_file))
    #     m = os.path.join(upload_file_path, news.news_file)
    #     print(m)
    #     os.system('rm ' + 'm')
    
    return redirect(url_for('admin.view_news'))

#---------------------------------------------------------

@admin.route('/admin/schedule')
@login_required
def view_schedule():
    return render_template('admin/admin_schedule.html', this_user=current_user)

#---------------------------------------------------------

@admin.route('/admin/subject')
@login_required
def view_subject():
    subjects = Subject.query.all()
    return render_template('admin/subject/admin_subject.html', this_user=current_user, subjects=subjects)


@admin.route('/admin/subject/create', methods=['GET', 'POST'])
@login_required
def create_subject():
    users = User.query.filter_by(user_role='tch').all()

    if request.method == 'POST':
        subject_id = request.form.get('s_id')
        subject_name = request.form.get('s_name')
        subject_teacher = request.form.get('s_teacher')
        
        if not subject_id or not subject_name or not subject_teacher:
            flash('Field canot be empty')
        else:
            new_subject = Subject(subject_id=subject_id, subject_name=subject_name, subject_teacher=subject_teacher)
            db.session.add(new_subject)
            db.session.commit()

            return redirect(url_for('admin.view_subject'))
    return render_template('admin/subject/create_subject.html', this_user=current_user, users=users)


#---------------------------------------------------------

@admin.route('/admin/user')
@login_required
def view_user():
    users = User.query.all()
    return render_template('admin/user/admin_user.html', this_user=current_user, users=users)


@admin.route('/admin/user/create', methods=['GET', 'POST'])
@login_required
def create_user():
    if request.method == 'POST':
        user_id = request.form.get('u_id')
        user_name = request.form.get('u_name')
        user_role = request.form.get('u_role')
        password = request.form.get('password')

        if not user_id or not user_name or not user_role or not password:
            flash('Field canot be empty')
        else:
            new_user = User(user_id=user_id, user_name=user_name, user_role=user_role, password=password)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('admin.view_user'))
    return render_template('admin/user/create_user.html', this_user=current_user)


@admin.route('/<int:id>/admin/user/update', methods=['GET', 'POST'])
@login_required
def update_user(id):
    if request.method == 'POST':
        user_id = request.form.get('u_id')
        user_name = request.form.get('u_name')
        user_role = request.form.get('u_role')
        password = request.form.get('password')

        if not user_id or not user_name or not user_role or not password:
            flash('Field canot be empty')
        else:
            user = User.query.filter_by(id=id).first()
            user.user_id = user_id
            user.user_name = user_name
            user.user_role = user_role
            user.password = password
            db.session.commit()

            return redirect(url_for('admin.view_user'))
    return render_template('admin/user/update_user.html', this_user=current_user, user=User.query.filter_by(id=id).first())


@admin.route('/<int:id>/admin/user/delete', methods=['GET', 'POST'])
@login_required
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('admin.view_user'))

#---------------------------------------------------------