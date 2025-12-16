from sqlalchemy import func
from db import db
from models.order import Order
from models.user import User

class OrderRepository:

    @staticmethod
    def total_by_user():
        return (
            db.session.query(
                User.name,
                func.sum(Order.amount).label("total")
            )
            .join(Order)
            .group_by(User.id)
            .all()
        )

    @staticmethod
    def orders_by_status(status):
        return (
            db.session.query(Order)
            .filter(Order.status == status)
            .all()
        )

    @staticmethod
    def average_order_value():
        return db.session.query(
            func.avg(Order.amount)
        ).scalar()

    @staticmethod
    def users_with_min_orders(min_orders: int):
        subquery = (
            db.session.query(
                Order.user_id,
                func.count(Order.id).label("qtd")
            )
            .group_by(Order.user_id)
            .subquery()
        )

        return (
            db.session.query(User)
            .join(subquery, User.id == subquery.c.user_id)
            .filter(subquery.c.qtd >= min_orders)
            .all()
        )
