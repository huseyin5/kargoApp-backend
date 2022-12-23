from .ma import ma
from db import KargoBilgileri
from .GondericiBilgileriSema import GondericiBilgileriSema


class KargolarVeGondericilerSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = KargoBilgileri

    GondericiBilgileri = ma.Nested(GondericiBilgileriSema, many=True)
