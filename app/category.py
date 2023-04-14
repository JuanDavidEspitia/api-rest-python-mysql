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


class Categoria(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_nom = db.Column(db.String(100))
    cat_desp = db.Column(db.String(100))

    def __init__(self, cat_nom, cat_desp):
        self.cat_nom = cat_nom
        self.cat_desp = cat_desp


# Crea las tablas
db.create_all()


# Mensaje de Bienvenida
@app.route("/", methods=["GET"])
def index():
    return jsonify({"Mensaje": "Bienvenido al curso de API Rest Python"})


if __name__ == "__main__":
    app.run(debug=True)
