from typing import List
from flask import abort
from app.models import db
from app.models.OrderItem import OrderItem

def list_order_items() -> List[OrderItem]:
    return OrderItem.query.all()

def get_order_item_by_id(order_item_id: int) -> OrderItem:
    item = OrderItem.query.get(order_item_id)
    if not item:
        abort(404, f"OrderItem {order_item_id} not found")
    return item

def list_order_items_for_order(order_id: int) -> List[OrderItem]:
    return OrderItem.query.filter_by(order_id=order_id).all()

def create_order_item(data: dict) -> OrderItem:
    item = OrderItem(**data)
    db.session.add(item)
    db.session.commit()
    return item

def update_order_item(order_item_id: int, data: dict) -> OrderItem:
    item = get_order_item_by_id(order_item_id)
    for key, value in data.items():
        setattr(item, key, value)
    db.session.commit()
    return item

def delete_order_item(order_item_id: int) -> None:
    item = get_order_item_by_id(order_item_id)
    db.session.delete(item)
    db.session.commit()