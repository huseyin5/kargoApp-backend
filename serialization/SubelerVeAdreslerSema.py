from .ma import ma
from db import SubeBilgileri
from .AdresSema import AdresSema


class SubelerVeAdreslerSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SubeBilgileri

    adresler = ma.Nested(AdresSema, many=True)
