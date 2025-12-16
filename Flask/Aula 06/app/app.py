from flask import Flask
from db import db
from routes.users import users_bp
from routes.analytics import analytics_bp

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(analytics_bp, url_prefix="/analytics")

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
