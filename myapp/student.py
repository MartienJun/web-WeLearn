import os
from myapp import db, files
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from myapp.models import Schedule, User, News, Subject, Profile_Employee, Class


student = Blueprint('student', __name__)


@student.route('/')
@login_required
def student_dashboard():
    return redirect(url_for('student.view_news'))

#---------------------------------------------------------

@student.route('/student/news')
@login_required
def view_news():
    news = News.query.all()
    return render_template('student/news/student_news.html', news=news)

#---------------------------------------------------------

@student.route('/student/profile', methods=['GET', 'POST'])
@login_required
def profile():
    profile = Profile_Employee.query.filter_by(employee_id=current_user.user_id).first()
    return render_template('student/student_profile.html', profile=profile)


@student.route('/student/profile/update', methods=['GET', 'POST'])
@login_required
def update_profile():
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

            return redirect(url_for('student.profile'))

            
    return render_template('student/update_student_profile.html')


@student.route('/student/schedule')
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

    return render_template('student/schedule/student_schedule.html', subjects=subjects, schedule_dict=schedule_dict, all_class=all_class, users=users)