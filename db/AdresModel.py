from sqlalchemy import Column, Integer, String

from .db import db


class Adres(db.Model):
    __tablename__ = 'adresler'

    adres_id = Column(Integer, primary_key=True)
    adres_turu = Column(String)
    adres = Column(String)
    adres_il = Column(String)
    adres_postaKodu = Column(String(5))
