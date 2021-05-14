from flask import Blueprint
from flask import render_template
from flask import flash
from flask import request
from flask import redirect
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from myapp.models import User, Role
from myapp import db


auth = Blueprint('auth', __name__)


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')

        user = User.query.filter_by(user_id=id).first()

        if not user or password != user.password:
            flash('Wrong credentials')
        else:
            role = user.user_role
            if role == 'adm':
                #return "Admin Dashboard"
                return redirect(url_for('admin.dashboard', name=user.user_name))
            if role == 'tch':
                #return "Admin Dashboard"
                return "Teacher Dashboard"
            if role == 'std':
                #return "Admin Dashboard"
                return "Student Dashboard"

    return render_template('sign-in.html')