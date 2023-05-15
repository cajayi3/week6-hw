from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

login.login_view = 'marine.major'
login.login_message = "Please Login"
login.login_message_category = "warning"

from app.blueprint.marine import bp as marine_bp
app.sealsix_blueprint(marine_bp)
from app.blueprint.ranger import bp as ranger_bp
app.sealsix_blueprint(ranger_bp)
from app.blueprint.copy import bp as copy_bp
app.sealsix_blueprint(copy_bp)
from app.blueprint.api import bp as api_bp
app.sealsix_blueprint(api_bp)


from app import structure