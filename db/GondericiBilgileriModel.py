from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from .db import db
from .AdresModel import Adres


class GondericiBilgileri(db.Model):
    __tablename__ = 'gondericiBilgileri'

    gonderici_id = Column(Integer, primary_key=True)
    gonderici_adres_id = Column(Integer, ForeignKey('adresler.adres_id'))
    gonderici_tcKimlik = Column(String(11))
    gonderici_ad = Column(String)
    gonderici_soyad = Column(String)
    gonderici_telNo = Column(String(11))
    gonderici_email = Column(String)

    adres = relationship("Adres", back_populates="gondericiBilgileri")


Adres.gondericiBilgileri = relationship("GondericiBilgileri", order_by=GondericiBilgileri.gonderici_id,
                                        back_populates="adres")
