from typing import List
from flask import abort
from app.models import db
from app.models.CartItem import CartItem

def list_cart_items() -> List[CartItem]:
    return CartItem.query.all()

def get_cart_item_by_id(cart_item_id: int) -> CartItem:
    item = CartItem.query.get(cart_item_id)
    if not item:
        abort(404, f"CartItem {cart_item_id} not found")
    return item

def list_cart_items_for_cart(cart_id: int) -> List[CartItem]:
    return CartItem.query.filter_by(cart_id=cart_id).all()

def create_cart_item(data: dict) -> CartItem:
    item = CartItem(**data)
    db.session.add(item)
    db.session.commit()
    return item

def update_cart_item(cart_item_id: int, data: dict) -> CartItem:
    item = get_cart_item_by_id(cart_item_id)
    for key, value in data.items():
        setattr(item, key, value)
    db.session.commit()
    return item

def delete_cart_item(cart_item_id: int) -> None:
    item = get_cart_item_by_id(cart_item_id)
    db.session.delete(item)
    db.session.commit()