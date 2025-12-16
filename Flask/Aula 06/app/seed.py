from datetime import datetime, timedelta
from app import create_app
from db import db
from models.user import User
from models.order import Order

app = create_app()

with app.app_context():
    # Recria a base para fins didáticos
    db.drop_all()
    db.create_all()

    # Usuários
    u1 = User(name="Alice", city="Goiânia")
    u2 = User(name="Bob", city="Anápolis")
    u3 = User(name="Carlos", city="Goiânia")

    db.session.add_all([u1, u2, u3])
    db.session.commit()

    now = datetime.now()

    # Pedidos
    orders = [
        Order(
            total=150.0,
            created_at=now - timedelta(days=10),
            user_id=u1.id
        ),
        Order(
            total=230.5,
            created_at=now - timedelta(days=5),
            user_id=u1.id
        ),
        Order(
            total=99.9,
            created_at=now - timedelta(days=7),
            user_id=u2.id
        ),
        Order(
            total=450.0,
            created_at=now - timedelta(days=1),
            user_id=u3.id
        ),
        Order(
            total=120.0,
            created_at=now,
            user_id=u3.id
        ),
    ]

    db.session.add_all(orders)
    db.session.commit()

    print("Seed executado com sucesso.")
