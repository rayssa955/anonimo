from flask import Blueprint, render_template, request
from database import db
from models import Voo, Piloto, Aviao

voos_bp = Blueprint("voos", __name__)

@voos_bp.route("/voos", methods=["GET", "POST"])
def voos():

    if request.method == "POST":

        origem = request.form["origem"]
        destino = request.form["destino"]
        piloto_id = request.form["piloto_id"]
        aviao_id = request.form["aviao_id"]

        novo_voo = Voo(
            origem=origem,
            destino=destino,
            piloto_id=piloto_id,
            aviao_id=aviao_id
        )

        db.session.add(novo_voo)
        db.session.commit()

    lista_voos = Voo.query.all()
    pilotos = Piloto.query.all()
    avioes = Aviao.query.all()

    return render_template(
        "voos.html",
        voos=lista_voos,
        pilotos=pilotos,
        avioes=avioes
    )