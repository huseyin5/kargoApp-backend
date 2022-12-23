from .ma import ma
from db import GondericiBilgileri


class GondericiBilgileriSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GondericiBilgileri
        load_instance = True
