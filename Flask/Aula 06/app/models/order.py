from db import db

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Float)
    created_at = db.Column(db.DateTime)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    user = db.relationship("User", back_populates="orders")

    def __repr__(self):
        return f"<Order {self.id} - {self.amount}>"
