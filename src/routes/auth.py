import json

from flask import Blueprint
from flask import jsonify
from flask import request
import psycopg2
from flask_jwt_extended import create_access_token

from src.static import get_db_connection

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.post("/authenticate")
def authenticate():
    try:
        username = request.form["username"]
    except KeyError:
        return jsonify(
            {
                "name": "Bad Request",
                "msg": "Need username to be authenticated.",
                "solution": "Try again.",
                "status_code": 400,
            }
        )
    

       # Connexion à la base de données RDS
    conn = get_db_connection()
    cur = conn.cursor()

    # Vérifiez si l'utilisateur existe
    cur.execute('SELECT id FROM users WHERE username = %s', (username,))
    result = cur.fetchone()

    if result:
        user_id = result[0]
    else:
        # Si l'utilisateur n'existe pas, créez un nouvel utilisateur
        cur.execute('INSERT INTO users (username) VALUES (%s) RETURNING id', (username,))
        user_id = cur.fetchone()[0]

    # Création du token d'accès
    identity = {"id": user_id, "username": username}
    access_token = create_access_token(identity=identity)

    response = {"success": True, "return": {"access": access_token}, "code": 200}

    conn.commit()
    cur.close()
    conn.close()

    return jsonify(response)
