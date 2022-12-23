from flask import Blueprint
from .adresler import adres_bp
from .aliciBilgileri import alici_bp
from .gondericiBilgileri import gonderici_bp
from .subeBilgileri import sube_bp
from .kargoBilgileri import kargo_bp

apiv1_bp = Blueprint("apiv1", __name__)
apiv1_bp.register_blueprint(adres_bp, url_prefix="/adresler")
apiv1_bp.register_blueprint(alici_bp, url_prefix="/alici")
apiv1_bp.register_blueprint(gonderici_bp, url_prefix="/gonderici")
apiv1_bp.register_blueprint(sube_bp, url_prefix="/sube")
apiv1_bp.register_blueprint(kargo_bp, url_prefix='/kargo')
