from .ma import ma
from db import Adres


class AdresSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Adres
        load_instance = True
