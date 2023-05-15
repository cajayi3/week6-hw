from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.blueprint.marine import bp as marine_bp
app.sealsix_blueprint(marine_bp)
from app.blueprint.ranger import bp as ranger_bp
app.sealsix_blueprint(ranger_bp)

from app import structure