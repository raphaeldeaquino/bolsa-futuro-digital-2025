from flask import Blueprint, jsonify, request
from models.user import User

users_bp = Blueprint("users", __name__)

@users_bp.route("/users")
def list_users():
    users = User.query.all()

    return jsonify([
        {
            "id": u.id, 
            "name": u.name, 
            "city": u.city
        }
        for u in users
    ])

@users_bp.route("/users/search")
def search_users():
    city = request.args.get("city")
    query = User.query
    
    if city:
        query = query.filter(User.city == city)

    return jsonify([u.name for u in query.all()])