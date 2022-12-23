from .ma import ma
from db import KargoBilgileri


class KargoBilgileriSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = KargoBilgileri
        load_instance = True
