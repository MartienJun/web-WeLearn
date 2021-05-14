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
from flask_login import login_user, logout_user, current_user, login_required


auth = Blueprint('auth', __name__)


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')

        user = User.query.filter_by(user_id=id).first()
        role = user.user_role

        if not user or password != user.password:
            flash('Wrong credentials')
        else:
            #Remeber the user
            login_user(user, remember=True)
            
            if role == 'adm':
                return redirect(url_for('admin.dashboard'))
            elif role == 'tch':
                return "Teacher Dashboard "
            else:
                return "Student Dashboard "

    return render_template('sign-in.html')


@auth.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('auth.signin'))