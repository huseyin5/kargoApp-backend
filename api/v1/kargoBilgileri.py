from flask import Blueprint, request, jsonify
from db import db, KargoBilgileri
from serialization import KargolarSema, KargoBilgileriSema, KargolarVeAlicilarSema
from utility import filtrele

kargo_bp = Blueprint("kargoBilgileri_islemleri", __name__)


@kargo_bp.route('/', methods=['GET'])
def tum_kargoBilgileri():
    kargolar = filtrele(KargoBilgileri).all()
    # kargoBilgileri = db.session.execute(db.select(KargoBilgileri)).scalars()
    sema = KargolarSema()

    return sema.dump(kargolar, many=True)


@kargo_bp.route('/<int:id>', methods=['GET'])
def kargo_detay(id):
    kargo = db.get_or_404(KargoBilgileri, id)
    sema = KargoBilgileriSema()
    return sema.dump(kargo)


@kargo_bp.route('/', methods=['POST'])
def kargo_ekle():
    kargo_bilgileri = request.json
    kargo = KargoBilgileri(**kargo_bilgileri)
    db.session.add(kargo)
    db.session.commit()

    sema = KargoBilgileriSema()
    return sema.dump(kargo)


@kargo_bp.route('/<int:id>', methods=['PUT'])
def kargo_guncelle(id):
    kargo = filtrele(KargoBilgileri).filter(KargoBilgileri.kargo_id == id).one_or_none()
    yeni_kargo_bilgileri = request.json

    sema = KargoBilgileriSema()
    yeni_kargo = sema.load(yeni_kargo_bilgileri, instance=kargo, session=db.session)
    db.session.commit()

    return sema.dump(yeni_kargo)


@kargo_bp.route('/<int:id>', methods=['DELETE'])
def kargo_sil(id):
    kargo = db.get_or_404(KargoBilgileri, id)
    db.session.delete(kargo)
    db.session.commit()
    return jsonify({'sonuc': 'TAMAM'})
