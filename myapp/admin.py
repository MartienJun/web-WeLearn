import os
from flask import Blueprint, render_template, flash, redirect, url_for, request
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from myapp.models import Schedule, User, News, Subject, Profile_Employee, Class, Module
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
    return render_template('admin/news/admin_news.html', news=news)


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
    return render_template('admin/news/create_news.html')


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
    return render_template('admin/news/update_news.html', news=News.query.filter_by(id=id).first())


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
    users = User.query.filter_by(user_role='tch').all()
    schedules = Schedule.query.all()
    all_class = Class.query.all()
    subjects = Subject.query.all()
    
    schedule_dict = {}
    for s in schedules: 
        if s.schedule_class in schedule_dict:
            schedule_dict[s.schedule_class].append(s)
        else:
            schedule_dict[s.schedule_class] = [s]

    return render_template('admin/schedule/admin_schedule.html', subjects=subjects, schedule_dict=schedule_dict, all_class=all_class, users=users)


@admin.route('/admin/schedule/create', methods=['GET', 'POST'])
@login_required
def create_schedule():
    subjects = Subject.query.all()
    all_class = Class.query.all()

    if request.method == 'POST':
        schedule_class = request.form.get('s_class')
        schedule_day = request.form.get('s_day')
        schedule_start = request.form.get('s_start')
        schedule_end = request.form.get('s_end')
        subject = request.form.get('s_subject')
        
        if not schedule_class or not schedule_day or not schedule_start or not schedule_end or not subject:
            flash('Field canot be empty')
        else:
            new_schedule = Schedule(schedule_class=schedule_class, day=schedule_day, start_time=schedule_start, end_time=schedule_end, subject=subject)
            db.session.add(new_schedule)
            db.session.commit()

            return redirect(url_for('admin.view_schedule'))
    return render_template('admin/schedule/create_schedule.html', subjects=subjects, all_class=all_class)


@admin.route('/<int:id>/admin/schedule/update', methods=['GET', 'POST'])
@login_required
def update_schedule(id):
    all_class = Class.query.all()
    subjects = Subject.query.all()
    schedule = Schedule.query.filter_by(id=id).first()

    if request.method == 'POST':
        schedule_class = request.form.get('s_class')
        schedule_day = request.form.get('s_day')
        schedule_start = request.form.get('s_start')
        schedule_end = request.form.get('s_end')
        subject = request.form.get('s_subject')
        
        if not schedule_class or not schedule_day or not schedule_start or not schedule_end or not subject:
            flash('Field canot be empty')
        else:
            new_schedule = Schedule(schedule_class=schedule_class, day=schedule_day, start_time=schedule_start, end_time=schedule_end, subject=subject)
            db.session.add(new_schedule)
            db.session.commit()

            return redirect(url_for('admin.view_schedule'))
    return render_template('admin/schedule/update_schedule.html', schedule=schedule, all_class=all_class, subjects=subjects)



@admin.route('/<int:id>/admin/schedule/delete', methods=['GET', 'POST'])
@login_required
def delete_schedule(id):
    schedule = Schedule.query.filter_by(id=id).first()
    db.session.delete(schedule)
    db.session.commit()
    return redirect(url_for('admin.view_schedule'))

#---------------------------------------------------------

@admin.route('/admin/subject')
@login_required
def view_subject():
    users = User.query.filter_by(user_role='tch').all()
    subjects = Subject.query.all()
    return render_template('admin/subject/admin_subject.html', subjects=subjects, users=users)


@admin.route('/admin/subject/create', methods=['GET', 'POST'])
@login_required
def create_subject():
    users = User.query.filter_by(user_role='tch').all()

    if request.method == 'POST':
        subject_id = request.form.get('s_id')
        subject_name = request.form.get('s_name')
        subject_teacher = request.form.get('s_teacher')
        sks = request.form.get('sks')
        
        if not subject_id or not subject_name or not subject_teacher or not sks:
            flash('Field canot be empty')
        else:
            new_subject = Subject(subject_id=subject_id, subject_name=subject_name, subject_teacher=subject_teacher, sks=sks)
            db.session.add(new_subject)
            db.session.commit()

            return redirect(url_for('admin.view_subject'))
    return render_template('admin/subject/create_subject.html', users=users)


@admin.route('/<int:id>/admin/subject/update', methods=['GET', 'POST'])
@login_required
def update_subject(id):
    users = User.query.filter_by(user_role='tch').all()

    if request.method == 'POST':
        subject_id = request.form.get('s_id')
        subject_name = request.form.get('s_name')
        subject_teacher = request.form.get('s_teacher')
        sks = request.form.get('sks')

        if not subject_id or not subject_name or not subject_teacher or not sks:
            flash('Field canot be empty')
        else:
            subject = Subject.query.filter_by(id=id).first()
            subject.subject_id = subject_id
            subject.subject_name = subject_name
            subject.subject_teacher = subject_teacher
            subject.sks = sks
            db.session.commit()

            return redirect(url_for('admin.view_subject'))
    return render_template('admin/subject/update_subject.html', users=users, subject=Subject.query.filter_by(id=id).first())


@admin.route('/<int:id>/admin/subject/delete', methods=['GET', 'POST'])
@login_required
def delete_subject(id):
    subject = Subject.query.filter_by(id=id).first()
    db.session.delete(subject)
    db.session.commit()
    return redirect(url_for('admin.view_subject'))

#---------------------------------------------------------

@admin.route('/admin/module/')
def view_module():
    subjects = Subject.query.all()
    modules = Module.query.all()
    return render_template('admin/module/view_module.html', subjects=subjects, modules=modules)


#---------------------------------------------------------

@admin.route('/admin/user')
@login_required
def view_user():
    users = User.query.all()
    return render_template('admin/user/admin_user.html', users=users)


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
    return render_template('admin/user/update_user.html', user=User.query.filter_by(id=id).first())


@admin.route('/<int:id>/admin/user/delete', methods=['GET', 'POST'])
@login_required
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('admin.view_user'))

#---------------------------------------------------------

@admin.route('/admin/profile', methods=['GET', 'POST'])
@login_required
def profile():
    profile = Profile_Employee.query.filter_by(employee_id=current_user.user_id).first()
    return render_template('admin/admin_profile.html', profile=profile)


@admin.route('/admin/profile/update', methods=['GET', 'POST'])
@login_required
def update_profile():
    profile = Profile_Employee.query.filter_by(employee_id=current_user.id).first()
    
    if request.method == 'POST':
        name = request.form.get('p_name')
        role = request.form.get('p_role')
        email = request.form.get('p_email')
        telp = request.form.get('p_telp')

        if not name or not role or not email or not telp:
            flash('Field canot be empty')
        else:
            user = User.query.filter_by(id=current_user.id).first()
            user.user_name = name
            user.user_role = role

            profile = Profile_Employee.query.filter_by(employee_id=user.user_id).first()
            if profile is not None:
                profile.email = email
                profile.telp = telp
            else:
                profile = Profile_Employee(
                    employee_id = current_user.user_id,
                    email = email,
                    telp = telp
                )
                db.session.add(profile)
            
            db.session.commit()

            return redirect(url_for('admin.profile'))
    return render_template('admin/update_admin_profile.html', profile=profile)