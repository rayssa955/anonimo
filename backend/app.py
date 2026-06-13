from flask import Flask, render_template
from database import db
from routes.avioes import avioes_bp
from models import Aviao, Piloto, Aeroporto, Voo
from routes.pilotos import pilotos_bp
from routes.aeroportos import aeroportos_bp
from routes.voos import voos_bp
app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../database/aviacao.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(avioes_bp)
app.register_blueprint(pilotos_bp)
app.register_blueprint(aeroportos_bp)
app.register_blueprint(voos_bp)

with app.app_context():
    from models import Aviao
    db.create_all()

@app.route("/")
def home():

    total_avioes = Aviao.query.count()
    total_pilotos = Piloto.query.count()
    total_aeroportos = Aeroporto.query.count()
    total_voos = Voo.query.count()

    return render_template(
        "index.html",
        total_avioes=total_avioes,
        total_pilotos=total_pilotos,
        total_aeroportos=total_aeroportos,
        total_voos=total_voos
    )
if __name__ == "__main__":
    app.run(debug=True)