from flask import Blueprint
from .v1 import apiv1_bp

api_bp = Blueprint("api", __name__)
api_bp.register_blueprint(apiv1_bp, url_prefix="/v1")
