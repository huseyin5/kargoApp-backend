from .ma import ma
from db import GondericiBilgileri
from .AdresSema import AdresSema


class GondericilerVeAdreslerSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GondericiBilgileri

    adresler = ma.Nested(AdresSema)
