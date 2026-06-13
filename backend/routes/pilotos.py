from flask import Blueprint, render_template, request
from database import db
from models import Piloto

pilotos_bp = Blueprint("pilotos", __name__)

@pilotos_bp.route("/pilotos", methods=["GET", "POST"])
def pilotos():

    if request.method == "POST":

        nome = request.form["nome"]
        licenca = request.form["licenca"]

        novo_piloto = Piloto(
            nome=nome,
            licenca=licenca
        )

        db.session.add(novo_piloto)
        db.session.commit()

    lista_pilotos = Piloto.query.all()

    return render_template(
        "pilotos.html",
        pilotos=lista_pilotos
    )