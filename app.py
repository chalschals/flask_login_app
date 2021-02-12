from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'cjaSdh*__&RT&%)_78'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #if we import these at top it will throw error
    #because these 3 files are using DB from this file itslef so we first need to initialise this file with db
    from auth import auth as auth_blueprint
    from main import main as main_blueprint
    from models import User


    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))


    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    return app