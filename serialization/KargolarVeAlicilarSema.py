from .ma import ma
from db import KargoBilgileri
from .AliciBilgileriSema import AliciBilgileriSema


class KargolarVeAlicilarSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = KargoBilgileri

    alicilar = ma.Nested(AliciBilgileriSema, many=True)
