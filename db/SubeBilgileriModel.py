from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .db import db
from .AdresModel import Adres


class SubeBilgileri(db.Model):
    __tablename__ = 'subeBilgileri'

    sube_id = Column(Integer, primary_key=True)
    sube_ad = Column(String)
    sube_adres_id = Column(Integer, ForeignKey('adresler.adres_id'))
    sube_telNo = Column(String(11))
    sube_yetkilisi = Column(String)

    adres = relationship("Adres", back_populates="subeBilgileri")


Adres.subeBilgileri = relationship("SubeBilgileri", order_by=SubeBilgileri.sube_id, back_populates="adres")
