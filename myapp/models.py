from myapp import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(7), nullable=False)
    user_name = db.Column(db.String(255), nullable=False)
    user_role = db.Column(db.String(7), db.ForeignKey('role.role_id', onupdate='CASCADE', ondelete='NO ACTION'), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return '<User %s>' % self.user_name

class Role(db.Model):
    role_id = db.Column(db.String(7), primary_key=True)
    role_name = db.Column(db.String(255), nullable=False)
    user = db.relationship('User', backref='role', lazy=True)

    def __repr__(self) -> str:
        return  '<Role %s>' % self.role_name