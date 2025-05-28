from typing import List
from flask import abort
from app.models import db
from app.models.Order import Order

def list_orders() -> List[Order]:
    return Order.query.all()

def get_order_by_id(order_id: int) -> Order:
    order = Order.query.get(order_id)
    if not order:
        abort(404, f"Order {order_id} not found")
    return order

def list_orders_by_user(user_id: int) -> List[Order]:
    return Order.query.filter_by(user_id=user_id).all()

def list_orders_by_date_range(start, end) -> List[Order]:
    return Order.query.filter(
        Order.created_at >= start,
        Order.created_at <= end
    ).all()

def create_order(data: dict) -> Order:
    order = Order(**data)
    db.session.add(order)
    db.session.commit()
    return order

def update_order(order_id: int, data: dict) -> Order:
    order = get_order_by_id(order_id)
    for key, value in data.items():
        setattr(order, key, value)
    db.session.commit()
    return order

def delete_order(order_id: int) -> None:
    order = get_order_by_id(order_id)
    db.session.delete(order)
    db.session.commit()