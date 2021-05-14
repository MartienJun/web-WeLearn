from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
DB_NAME = 'welearn.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'welearn welearn welearn'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    migrate = Migrate(app, db)

    #Import models
    from myapp.models import User, Role
    
    #Import blueprint
    from myapp.auth import auth
    app.register_blueprint(auth, url_prefix='/')

    from myapp.admin import admin
    app.register_blueprint(admin, url_prefix='/')

    return app