from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from .db import db
from .AdresModel import Adres


class AliciBilgileri(db.Model):
    __tablename__ = 'aliciBilgileri'

    alici_id = Column(Integer, primary_key=True)
    alici_adres_id = Column(Integer, ForeignKey('adresler.adres_id'))
    alici_tcKimlik = Column(String(11))
    alici_ad = Column(String)
    alici_soyad = Column(String)
    alici_telNo = Column(String(11))
    alici_email = Column(String)

    adres = relationship("Adres", back_populates="aliciBilgileri")


Adres.aliciBilgileri = relationship("AliciBilgileri", order_by=AliciBilgileri.alici_id, back_populates="adres")
