from flask import Blueprint, request, jsonify
from db import db, GondericiBilgileri
from serialization import GondericiBilgileriSema, GondericilerVeAdreslerSema
from utility import filtrele

gonderici_bp = Blueprint("gondericiBilgi_islemleri", __name__)


@gonderici_bp.route('/', methods=['GET'])
def tum_gondericiBilgileri():
    gondericiBilgileri = filtrele(GondericiBilgileri).all()
    sema = GondericilerVeAdreslerSema()
    # gondericiBilgileri = db.session.execute(db.select(GondericiBilgileri)).scalars()
    # sema = GondericiBilgileriSema()
    return sema.dump(gondericiBilgileri, many=True)


@gonderici_bp.route('/<int:id>', methods=['GET'])
def gonderici_detay(id):
    gonderici = db.get_or_404(GondericiBilgileri, id)
    sema = GondericiBilgileriSema()
    return sema.dump(gonderici)


@gonderici_bp.route('/', methods=['POST'])
def gonderici_ekle():
    gonderici_bilgileri = request.json
    gonderici = GondericiBilgileri(**gonderici_bilgileri)
    db.session.add(gonderici)
    db.session.commit()

    sema = GondericiBilgileriSema()
    return sema.dump(gonderici)


@gonderici_bp.route('/<int:id>', methods=['PUT'])
def gonderici_guncelle(id):
    gonderici = filtrele(GondericiBilgileri).filter(GondericiBilgileri.gonderici_id == id).one_or_none()
    yeni_gonderici_bilgileri = request.json

    sema = GondericiBilgileriSema()
    yeni_gonderici = sema.load(yeni_gonderici_bilgileri, instance=gonderici, session=db.session)
    db.session.commit()

    return sema.dump(yeni_gonderici)


@gonderici_bp.route('/<int:id>', methods=['DELETE'])
def gonderici_sil(id):
    gonderici = db.get_or_404(GondericiBilgileri, id)
    db.session.delete(gonderici)
    db.session.commit()
    return jsonify({'sonuc': 'TAMAM'})
