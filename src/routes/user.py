import json
import psycopg2
from flask import Blueprint
from flask import jsonify
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from src.static import get_db_connection
from src.utils.misc import capitalize_name

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/id")
@jwt_required()
def get_user_id():
    conn = get_db_connection()
    cur = conn.cursor()

    # Recherche de l'utilisateur dans la base de données
    cur.execute('SELECT id FROM users WHERE username = %s', (current_user["username"],))
    result = cur.fetchone()

    if result:
        return jsonify({"id": result[0]}), 200
    else:
        return jsonify(
            {
                "name": "Bad Request",
                "msg": "User not found.",
                "solution": "Try again.",
                "status_code": 400,
            }
        ), 400


@user_bp.route("/hello")
@jwt_required()
def get_hello():
    return f"Hello {capitalize_name(current_user['username'])}"
