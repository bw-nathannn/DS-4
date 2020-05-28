# app/__init__.py

# Windows flask deployment
#> $env:FLASK_APP = "app" #> flask run
#

#> Import statements
import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

#> Import routes
from app.models import db, migrate
from app.routes.home_routes import home_routes
from app.routes.model_routes import model_routes

load_dotenv()


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configure the database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/database.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Configure routes
    app.register_blueprint(home_routes)
    app.register_blueprint(model_routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)