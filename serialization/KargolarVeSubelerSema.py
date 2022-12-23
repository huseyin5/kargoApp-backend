from .ma import ma
from db import KargoBilgileri
from .SubeBilgileriSema import SubeBilgileriSema


class KargolarVeSubelerSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = KargoBilgileri

    subeBilgileri = ma.Nested(SubeBilgileriSema, many=True)
