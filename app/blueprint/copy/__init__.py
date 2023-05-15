from flask import Blueprint

bp = Blueprint('copy', __name__, url_prefix='/copy')

from . import routes