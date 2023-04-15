# Importar Librerias Instaladas
# pip install flask
# pip install flask-sqlalchemy   -----Para Conectar a una BD SQL
# pip install flask-marshmallow  -----Definir Esquema con la BD
# pip install marshmallow-sqlalchemy
# pip install pymysql            ------Para Conectar a MySQL Driver MySQL

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Instancia de FLASK mi aplicacion
app = Flask(__name__)
# Cadena de conexion
# 'mysql+pymysql://[user]:[pwd]@localhost:3306/[base_de_datos]'
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root:admin1234@localhost:3306/bdpythonapi"
# Configuracion por defecto para no alertar o warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.app_context().push()

# Inicilizamos nuestro SQLAlchemy
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Creacion de tabla categoria
class Categoria(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_nom = db.Column(db.String(100))
    cat_desp = db.Column(db.String(100))

    def __init__(self, cat_nom, cat_desp):
        self.cat_nom = cat_nom
        self.cat_desp = cat_desp


# Crea las tablas
db.create_all()


# Esquema
class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ("cat_id", "cat_nom", "cat_desp")


# Una sola Respuesta
categoria_schema = CategoriaSchema()

# Cuando sean muchas respuestas
categorias_schema = CategoriaSchema(many=True)


# GET
@app.route("/categoria", methods=["GET"])
def get_categorias():
    all_categorias = Categoria.query.all()
    result = categorias_schema.dump(all_categorias)
    return jsonify(result)


# GET by ID
@app.route("/categoria/<id>", methods=["GET"])
def get_categoria_id(id):
    categoria = Categoria.query.get(id)
    return categoria_schema.jsonify(categoria)


# POST
@app.route("/categoria", methods=["POST"])
def insert_categoria():
    cat_nom = request.json["cat_nom"]
    cat_desp = request.json["cat_desp"]
    new_row = Categoria(cat_nom, cat_desp)

    db.session.add(new_row)
    db.session.commit()
    return categoria_schema.jsonify(new_row)


# PUT
@app.route("/categoria/<id>", methods=["PUT"])
def update_categoria(id):
    actualizarcategoria = Categoria.query.get(id)

    data = request.get_json(force=True)
    cat_nom = data["cat_nom"]
    cat_desp = data["cat_desp"]

    actualizarcategoria.cat_nom = cat_nom
    actualizarcategoria.cat_desp = cat_desp

    db.session.commit()

    return categoria_schema.jsonify(actualizarcategoria)


# DELETE
@app.route("/categoria/<id>", methods=["DELETE"])
def delete_categoria(id):
    eliminarcategoria = Categoria.query.get(id)
    db.session.delete(eliminarcategoria)
    db.session.commit()
    return categoria_schema.jsonify(eliminarcategoria)


# Mensaje de Bienvenida
@app.route("/", methods=["GET"])
def index():
    return jsonify({"Mensaje": "Bienvenido al curso de API Rest Python"})


if __name__ == "__main__":
    app.run(debug=True)
