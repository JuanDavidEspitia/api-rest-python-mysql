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
] = "mysql+pymysql://root:@localhost:3306/bdpythonapi"
# Configuracion por defecto para no alertar o warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Mensaje de Bienvenida
@app.route("/", methods=["GET"])
def index():
    return jsonify({"Mensaje": "Bienvenido al curso de API Rest Python"})


if __name__ == "__main__":
    app.run(debug=True)
