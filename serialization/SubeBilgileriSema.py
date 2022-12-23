from .ma import ma
from db import SubeBilgileri


class SubeBilgileriSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SubeBilgileri
        load_instance = True
