from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import nctu_oauth