from flask import Blueprint

bp = Blueprint('marine', __name__, url_prefix='/marine')

from app.blueprint.marine import routes