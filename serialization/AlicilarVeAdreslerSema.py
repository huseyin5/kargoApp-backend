from .ma import ma
from db import AliciBilgileri
from .AdresSema import AdresSema


class AlicilarVeAdreslerSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AliciBilgileri

    adresler = ma.Nested(AdresSema)
