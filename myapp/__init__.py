import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads
from flask_uploads.extensions import DOCUMENTS, IMAGES

files = UploadSet('files', IMAGES + DOCUMENTS)
db = SQLAlchemy()
DB_NAME = 'welearn.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'welearn welearn welearn'
    
    #Upload folder config
    app.config['UPLOADED_FILES_DEST'] = os.path.realpath('.') + '/uploads'
    app.config['UPLOADED_FILES_ALLOW'] = ["JPEG", "JPG", "PNG", "PDF"]
    app.config['MAX_CONTENT_LENGTH'] = 10 * 1000 * 1000 #Max file size 10MB
    configure_uploads(app, files)

    #Database config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    migrate = Migrate(app, db)

    #Import models
    from myapp.models import User, Role, News, Subject, Module

    #Import blueprint
    from myapp.auth import auth
    app.register_blueprint(auth, url_prefix='/')

    from myapp.admin import admin
    app.register_blueprint(admin, url_prefix='/admin')

    from myapp.teacher import teacher
    app.register_blueprint(teacher, url_prefix='/teacher')

    from myapp.student import student
    app.register_blueprint(student, url_prefix='/student')

    #Login manager settings
    login_manager = LoginManager()
    login_manager.login_view = 'auth.signin'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app