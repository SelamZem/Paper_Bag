from typing import List
from flask import abort
from app.models import db
from app.models.Cart import Cart

def list_carts() -> List[Cart]:
    return Cart.query.all()

def get_cart_by_id(cart_id: int) -> Cart:
    cart = Cart.query.get(cart_id)
    if not cart:
        abort(404, f"Cart {cart_id} not found")
    return cart

def get_cart_by_user(user_id: int) -> Cart:
    cart = Cart.query.filter_by(user_id=user_id).first()
    if not cart:
        abort(404, f"Cart for user {user_id} not found")
    return cart

def create_cart(data: dict) -> Cart:
    cart = Cart(**data)
    db.session.add(cart)
    db.session.commit()
    return cart

def update_cart(cart_id: int, data: dict) -> Cart:
    cart = get_cart_by_id(cart_id)
    for key, value in data.items():
        setattr(cart, key, value)
    db.session.commit()
    return cart

def delete_cart(cart_id: int) -> None:
    cart = get_cart_by_id(cart_id)
    db.session.delete(cart)
    db.session.commit()