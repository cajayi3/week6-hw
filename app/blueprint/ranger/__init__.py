from flask import Blueprint

bp = Blueprint('ranger', __name__)

from app.blueprint.ranger import routes