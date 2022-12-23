from flask import Blueprint, request, jsonify
from db import db, SubeBilgileri
from serialization import SubeBilgileriSema
from utility import filtrele

sube_bp = Blueprint("subeBilgileri_islemleri", __name__)


@sube_bp.route('/', methods=['GET'])
def tum_subeBilgileri():
    subeBilgileri = filtrele(SubeBilgileri).all()
    sema = SubeBilgileriSema()
    # subeBilgileri = db.session.execute(db.select(SubeBilgileri)).scalars()
    # sema = SubeBilgileriSema()
    return sema.dump(subeBilgileri, many=True)


@sube_bp.route('/<int:id>', methods=['GET'])
def sube_detay(id):
    sube = db.get_or_404(SubeBilgileri, id)
    sema = SubeBilgileriSema()
    return sema.dump(sube)


@sube_bp.route('/', methods=['POST'])
def sube_ekle():
    sube_bilgileri = request.json
    sube = SubeBilgileri(**sube_bilgileri)
    db.session.add(sube)
    db.session.commit()

    sema = SubeBilgileriSema()
    return sema.dump(sube)


@sube_bp.route('/<int:id>', methods=['PUT'])
def sube_guncelle(id):
    sube = filtrele(SubeBilgileri).filter(SubeBilgileri.sube_id == id).one_or_none()
    yeni_sube_bilgileri = request.json

    sema = SubeBilgileriSema()
    yeni_sube = sema.load(yeni_sube_bilgileri, instance=sube, session=db.session)
    db.session.commit()

    return sema.dump(yeni_sube)


@sube_bp.route('/<int:id>', methods=['DELETE'])
def sube_sil(id):
    sube = db.get_or_404(SubeBilgileri, id)
    db.session.delete(sube)
    db.session.commit()
    return jsonify({'sonuç': ' TAMAM'})
