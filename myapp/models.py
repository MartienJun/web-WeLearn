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
    subject_id = db.Column(db.String(7), nullable=False)
    subject_name = db.Column(db.String(255), nullable=False)
    subject_teacher = db.Column(db.String(7), db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='SET NULL'), nullable=True)
    subject_name = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return  '<Role %s>' % self.subject_name


class Profile_Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(7), db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    telp = db.Column(db.String(15), unique=True, nullable=False)

    def __repr__(self) -> str:
        return  '<Role %s>' % self.employee_id
