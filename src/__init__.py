import os
from datetime import timedelta

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS  # type: ignore
from flask_jwt_extended import JWTManager
from src.routes.auth import auth_bp
from src.routes.user import user_bp
from src.utils.jwt import register_jwt_handlers

APP_ROOT = os.path.join(os.path.dirname(__file__), "../")
dotenv_path = os.path.join(APP_ROOT, ".env")
load_dotenv(dotenv_path)

application.config["DB_HOST"] = os.environ.get("DB_HOST")  
application.config["DB_USER"] = os.environ.get("DB_USER")  
application.config["DB_PASSWORD"] = os.environ.get("DB_PASSWORD")
application.config["DB_NAME"] = os.environ.get("DB_NAME")


application = Flask(__name__, instance_relative_config=True)


application.register_blueprint(auth_bp)
application.register_blueprint(user_bp)


application.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
application.config["JWT_SECRET_KEY"] = os.environ.get("SECRET_KEY", "SECRET_KEY")

jwt_manager = JWTManager(application)
register_jwt_handlers(jwt_manager)

CORS(application, expose_headers="Authorization", supports_credentials=True)
