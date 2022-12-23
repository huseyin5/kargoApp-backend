from .ma import ma
from db import KargoBilgileri
from .AliciBilgileriSema import AliciBilgileriSema
from .GondericiBilgileriSema import GondericiBilgileriSema
from .SubeBilgileriSema import SubeBilgileriSema


class KargolarSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = KargoBilgileri

    alicilar = ma.Nested(AliciBilgileriSema, many=True)
    gondericiler = ma.Nested(GondericiBilgileriSema, many=True)
    subeler = ma.Nested(SubeBilgileriSema, many=True)
