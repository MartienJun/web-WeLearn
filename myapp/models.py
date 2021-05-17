from sqlalchemy.orm import backref
from myapp import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(7), unique=True, nullable=False)
    user_name = db.Column(db.String(255), nullable=False)
    user_role = db.Column(db.String(7), db.ForeignKey('role.role_id', onupdate='CASCADE'), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    subject = db.relationship('Subject', backref='teacher', lazy=True)
    profile_employee = db.relationship('Profile_Employee', backref='employee', lazy=True)

    def __repr__(self) -> str:
        return '<User %s>' % self.user_name


class Role(db.Model):
    role_id = db.Column(db.String(7), primary_key=True)
    role_name = db.Column(db.String(255), nullable=False)
    user = db.relationship('User', backref='role', lazy=True)

    def __repr__(self) -> str:
        return  '<Role %s>' % self.role_name


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    news_title = db.Column(db.String(255), nullable=False)
    news_message = db.Column(db.String(255), nullable=False)
    news_file = db.Column(db.String(255), nullable=True)

    def __repr__(self) -> str:
        return  '<Role %s>' % self.news_title


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.String(7), unique=True, nullable=False)
    subject_name = db.Column(db.String(255), nullable=False)
    subject_teacher = db.Column(db.String(7), db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='SET NULL'), nullable=True)
    sks = db.Column(db.Integer, nullable=False)
    subject_name = db.Column(db.String(255), nullable=False)
    schedule = db.relationship('Schedule', backref='schedule_subject', lazy=True)
    subject_module = db.relationship('Module', backref='subject_module', lazy=True)

    def __repr__(self) -> str:
        return  '<Role %s>' % self.subject_name


class Profile_Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(7), db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    telp = db.Column(db.String(15), unique=True, nullable=False)

    def __repr__(self) -> str:
        return  '<Role %s>' % self.employee_id


class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.String(7), unique=True, nullable=False)
    class_name = db.Column(db.String(255), unique=True, nullable=False)
    schedule = db.relationship('Schedule', backref='schedule_c', lazy=True)

    def __repr__(self) -> str:
        return  '<Role %s>' % self.class_id


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schedule_class = db.Column(db.String(7), db.ForeignKey('class.class_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    day = db.Column(db.String(10), nullable=False)
    start_time = db.Column(db.String(10), nullable=False)
    end_time = db.Column(db.String(10), nullable=False)
    subject = db.Column(db.String(7), db.ForeignKey('subject.subject_id', onupdate='CASCADE', ondelete='SET NULL'), nullable=True)

    def __repr__(self) -> str:
        return  '<Role %s>' % self.schedule_class


class Module(db.Model):
    module_id = db.Column(db.String(7), db.ForeignKey('subject.subject_id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True, nullable=False)
    topic_1 = db.Column(db.String(255), nullable=True)
    about_topic_1 = db.Column(db.String(255), nullable=True)
    assignment_1 = db.Column(db.String(255), nullable=True)
    
    topic_2 = db.Column(db.String(255), nullable=True)
    about_topic_2 = db.Column(db.String(255), nullable=True)
    assignment_2 = db.Column(db.String(255), nullable=True)
    
    topic_3 = db.Column(db.String(255), nullable=True)
    about_topic_3 = db.Column(db.String(255), nullable=True)
    assignment_3 = db.Column(db.String(255), nullable=True)
    
    topic_4 = db.Column(db.String(255), nullable=True)
    about_topic_4 = db.Column(db.String(255), nullable=True)
    assignment_4 = db.Column(db.String(255), nullable=True)
    
    topic_5 = db.Column(db.String(255), nullable=True)
    about_topic_5 = db.Column(db.String(255), nullable=True)
    assignment_5 = db.Column(db.String(255), nullable=True)
    
    topic_6 = db.Column(db.String(255), nullable=True)
    about_topic_6 = db.Column(db.String(255), nullable=True)
    assignment_6 = db.Column(db.String(255), nullable=True)
    
    topic_7 = db.Column(db.String(255), nullable=True)
    about_topic_7 = db.Column(db.String(255), nullable=True)
    assignment_7 = db.Column(db.String(255), nullable=True)
    
    topic_8 = db.Column(db.String(255), nullable=True)
    about_topic_8 = db.Column(db.String(255), nullable=True)
    assignment_8 = db.Column(db.String(255), nullable=True)
    
    topic_9 = db.Column(db.String(255), nullable=True)
    about_topic_9 = db.Column(db.String(255), nullable=True)
    assignment_9 = db.Column(db.String(255), nullable=True)
    
    topic_10 = db.Column(db.String(255), nullable=True)
    about_topic_10 = db.Column(db.String(255), nullable=True)
    assignment_10 = db.Column(db.String(255), nullable=True)
    
    topic_11 = db.Column(db.String(255), nullable=True)
    about_topic_11 = db.Column(db.String(255), nullable=True)
    assignment_11 = db.Column(db.String(255), nullable=True)
    
    topic_12 = db.Column(db.String(255), nullable=True)
    about_topic_12 = db.Column(db.String(255), nullable=True)
    assignment_12 = db.Column(db.String(255), nullable=True)
    
    topic_13 = db.Column(db.String(255), nullable=True)
    about_topic_13 = db.Column(db.String(255), nullable=True)
    assignment_13 = db.Column(db.String(255), nullable=True)

    def __repr__(self) -> str:
        return  '<Module %s>' % self.module_id