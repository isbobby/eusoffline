
from flask import Flask
from eusoffline.config import Config
from eusoffline.extensions import db, login_manager
from flask_user import UserManager
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from eusoffline.main.routes import main

login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from eusoffline.models import BaseUser

@login_manager.user_loader
def user_loader(user_id):
    return BaseUser.query.get(user_id)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # pass our web app to the extension packages
    db.init_app(app)
    UserManager(app, db, BaseUser)

    # initialize admin
    admin = Admin(app, name='Eusoff line', template_mode='bootstrap3')

    app.register_blueprint(main)

    admin.add_view(ModelView(BaseUser, db.session))

    return app
