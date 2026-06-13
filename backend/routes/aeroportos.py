from flask import Blueprint, render_template, request
from database import db
from models import Aeroporto

aeroportos_bp = Blueprint("aeroportos", __name__)

@aeroportos_bp.route("/aeroportos", methods=["GET", "POST"])
def aeroportos():

    if request.method == "POST":

        nome = request.form["nome"]
        cidade = request.form["cidade"]

        novo_aeroporto = Aeroporto(
            nome=nome,
            cidade=cidade
        )

        db.session.add(novo_aeroporto)
        db.session.commit()

    lista_aeroportos = Aeroporto.query.all()

    return render_template(
        "aeroportos.html",
        aeroportos=lista_aeroportos
    )