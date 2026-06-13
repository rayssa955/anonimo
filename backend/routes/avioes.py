from flask import Blueprint, render_template, request
from database import db
from models import Aviao

avioes_bp = Blueprint("avioes", __name__)

@avioes_bp.route("/avioes", methods=["GET", "POST"])
def avioes():

    if request.method == "POST":

        modelo = request.form["modelo"]
        fabricante = request.form["fabricante"]
        capacidade = request.form["capacidade"]

        novo_aviao = Aviao(
            modelo=modelo,
            fabricante=fabricante,
            capacidade=capacidade
        )

        db.session.add(novo_aviao)
        db.session.commit()

    lista_avioes = Aviao.query.all()

    return render_template(
        "avioes.html",
        avioes=lista_avioes
    )