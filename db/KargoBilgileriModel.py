from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship

from .db import db
from .AliciBilgileriModel import AliciBilgileri
from .GondericiBilgileriModel import GondericiBilgileri
from .SubeBilgileriModel import SubeBilgileri


class KargoBilgileri(db.Model):
    __tablename__ = 'kargoBilgileri'

    kargo_id = Column(Integer, primary_key=True)
    kargo_alici_id = Column(Integer, ForeignKey('aliciBilgileri.alici_id'))
    kargo_gonderici_id = Column(Integer, ForeignKey('gondericiBilgileri.gonderici_id'))
    kargo_sube_id = Column(Integer, ForeignKey('subeBilgileri.sube_id'))
    kargo_tarihi = Column(DateTime)
    kargo_odemeTuru = Column(String)

    alici = relationship("AliciBilgileri", back_populates="kargoBilgileri")
    gonderici = relationship("GondericiBilgileri", back_populates="kargoBilgileri")
    sube = relationship("SubeBilgileri", back_populates="kargoBilgileri")


AliciBilgileri.kargoBilgileri = relationship("KargoBilgileri", back_populates="alici")
GondericiBilgileri.kargoBilgileri = relationship("KargoBilgileri", back_populates="gonderici")
SubeBilgileri.kargoBilgileri = relationship("KargoBilgileri", back_populates="sube")
