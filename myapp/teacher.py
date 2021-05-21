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

#---------------------------------------------------------

@teacher.route('/teacher/profile', methods=['GET', 'POST'])
@login_required
def profile():
    profile = Profile_Employee.query.filter_by(employee_id=current_user.user_id).first()
    return render_template('teacher/teacher_profile.html', profile=profile)


@teacher.route('/teacher/profile/update', methods=['GET', 'POST'])
@login_required
def update_profile():
    profile = Profile_Employee.query.filter_by(employee_id=current_user.user_id).first()

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

            return redirect(url_for('teacher.profile'))
    return render_template('teacher/update_teacher_profile.html', profile=profile)

#---------------------------------------------------------

@teacher.route('/teacher/schedule')
@login_required
def view_schedule():
    users = User.query.filter_by(user_role='tch').all()
    all_class = Class.query.all()
    profile = Profile_Employee.query.filter_by(employee_id=current_user.user_id).first()
    subjects = Subject.query.filter_by(subject_teacher=profile.employee_id).all()
    subject_filter=[]

    for subject in subjects:
        subject_filter.append(subject.subject_id)

    schedules = Schedule.query.filter(Schedule.subject.in_(subject_filter)).all()

    schedule_dict = {}
    for s in schedules: 
        if s.subject in schedule_dict:
            schedule_dict[s.subject].append(s)
        else:
            schedule_dict[s.subject] = [s]

    return render_template('teacher/schedule/teacher_schedule.html', subjects=subjects, schedule_dict=schedule_dict, all_class=all_class, users=users)
