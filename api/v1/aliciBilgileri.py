from flask import Blueprint, request, jsonify
from db import db, AliciBilgileri
from serialization import AliciBilgileriSema, AlicilarVeAdreslerSema
from utility import filtrele

alici_bp = Blueprint("aliciBilgi_islemleri", __name__)


@alici_bp.route('/', methods=['GET'])
def tum_aliciBilgileri():
    aliciBilgileri = filtrele(AliciBilgileri).all()
    sema = AlicilarVeAdreslerSema()
    # aliciBilgileri = db.session.execute(db.select(AliciBilgileri)).scalars()
    # sema = AliciBilgileriSema()
    return sema.dump(aliciBilgileri, many=True)


@alici_bp.route('/<int:id>', methods=['GET'])
def alici_detay(id):
    alici = db.get_or_404(AliciBilgileri, id)
    sema = AliciBilgileriSema()
    return sema.dump(alici)


@alici_bp.route('/', methods=['POST'])
def alici_ekle():
    alici_bilgileri = request.json
    alici = AliciBilgileri(**alici_bilgileri)
    db.session.add(alici)
    db.session.commit()

    sema = AliciBilgileriSema()
    return sema.dump(alici)


@alici_bp.route('/<int:id>', methods=['PUT'])
def alici_guncelle(id):
    alici = filtrele(AliciBilgileri).filter(AliciBilgileri.alici_id == id).one_or_none()
    yeni_alici_bilgileri = request.json

    sema = AliciBilgileriSema()
    yeni_alici = sema.load(yeni_alici_bilgileri, instance=alici, session=db.session)
    db.session.commit()

    return sema.dump(yeni_alici)


@alici_bp.route('/<int:id>', methods=['DELETE'])
def alici_sil(id):
    alici = db.get_or_404(AliciBilgileri, id)
    db.session.delete(alici)
    db.session.commit()
    return jsonify({'sonuc': 'TAMAM'})
