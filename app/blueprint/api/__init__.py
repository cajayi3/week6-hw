from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')

from app.blueprint.api import routes, marine_routes