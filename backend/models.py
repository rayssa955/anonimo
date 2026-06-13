from database import db

class Aviao(db.Model):
    __tablename__ = "avioes"

    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(100), nullable=False)
    fabricante = db.Column(db.String(100), nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)

class Piloto(db.Model):
    __tablename__ = "pilotos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    licenca = db.Column(db.String(50), nullable=False)

class Aeroporto(db.Model):
    __tablename__ = "aeroportos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)

class Voo(db.Model):
    __tablename__ = "voos"

    id = db.Column(db.Integer, primary_key=True)

    origem = db.Column(db.String(100), nullable=False)
    destino = db.Column(db.String(100), nullable=False)

    piloto_id = db.Column(
        db.Integer,
        db.ForeignKey("pilotos.id")
    )

    aviao_id = db.Column(
        db.Integer,
        db.ForeignKey("avioes.id")
    )

    piloto = db.relationship("Piloto")
    aviao = db.relationship("Aviao")