from flask import Blueprint, request, jsonify
from db import db, Adres
from serialization import AdresSema
from utility import filtrele

adres_bp = Blueprint("adres_islemleri", __name__)


@adres_bp.route('/', methods=['GET'])
def tum_adresler():
    adresler = filtrele(Adres).all()
    # adresler = db.session.execute(db.select(Adres)).scalars()
    sema = AdresSema()
    return sema.dump(adresler, many=True)


@adres_bp.route('/<int:id>', methods=['GET'])
def adres_detay(id):
    adres = db.get_or_404(Adres, id)
    sema = AdresSema()
    return sema.dump(adres)


@adres_bp.route('/', methods=['POST'])
def adres_ekle():
    adres_bilgileri = request.json
    adres = Adres(**adres_bilgileri)
    db.session.add(adres)
    db.session.commit()

    sema = AdresSema()
    return sema.dump(adres)


@adres_bp.route('/<int:id>', methods=['PUT'])
def adres_guncelle(id):
    adres = filtrele(Adres).filter(Adres.adres_id == id).one_or_none()
    yeni_adres_bilgileri = request.json

    sema = AdresSema()
    yeni_adres = sema.load(yeni_adres_bilgileri, instance=adres, session=db.session)
    db.session.commit()

    return sema.dump(yeni_adres)


@adres_bp.route('/<int:id>', methods=['DELETE'])
def adres_sil(id):
    adres = db.get_or_404(Adres, id)
    db.session.delete(adres)
    db.session.commit()
    return jsonify({'sonuc': 'TAMAM'})
