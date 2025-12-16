import os
from flask import Flask
from db import db
from routes.users import users_bp
from routes.analytics import analytics_bp

def create_app():
    app = Flask(__name__)

    # Garante que o banco fique no diretório instance
    basedir = os.path.abspath(os.path.dirname(__file__))
    instance_path = os.path.join(basedir, 'instance')
    
    # Cria o diretório instance se não existir
    os.makedirs(instance_path, exist_ok=True)
    
    database_path = os.path.join(instance_path, 'app.db')
    
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    print(f"📁 Database: {database_path}")
    db.init_app(app)

    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(analytics_bp, url_prefix="/analytics")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
