from flask import Blueprint, jsonify
from repositories.order_repository import OrderRepository

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route("/total-by-user", methods=["GET"])
def total_by_user():
    data = OrderRepository.total_by_user()
    return jsonify([
        {"user": name, "total": total}
        for name, total in data
    ])

@analytics_bp.route("/average-order", methods=["GET"])
def average_order():
    avg = OrderRepository.average_order_value()
    return jsonify({"average_order_value": avg})

@analytics_bp.route("/users-with-min-orders/<int:min_orders>", methods=["GET"])
def users_with_min_orders(min_orders):
    users = OrderRepository.users_with_min_orders(min_orders)
    return jsonify([
        {"id": u.id, "name": u.name}
        for u in users
    ])
