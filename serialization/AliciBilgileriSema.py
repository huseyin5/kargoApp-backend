from .ma import ma
from db import AliciBilgileri


class AliciBilgileriSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AliciBilgileri
        load_instance = True
