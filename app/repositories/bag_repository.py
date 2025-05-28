from typing import List
from flask import abort
from app.models import db
from app.models.Bag import Bag

def list_bags() -> List[Bag]:
    return Bag.query.all()

def get_bag_by_id(bag_id: int) -> Bag:
    bag = Bag.query.get(bag_id)
    if not bag:
        abort(404, f"Bag {bag_id} not found")
    return bag

def list_bags_by_category(category_id: int) -> List[Bag]:
    return Bag.query.filter_by(category_id=category_id).all()

def list_available_bags() -> List[Bag]:
    return Bag.query.filter(Bag.stock_quantity > 0).all()

def search_bags(keyword: str) -> List[Bag]:
    return Bag.query.filter(
        Bag.name.ilike(f"%{keyword}%") |
        Bag.description.ilike(f"%{keyword}%")
    ).all()

def create_bag(data: dict) -> Bag:
    bag = Bag(**data)
    db.session.add(bag)
    db.session.commit()
    return bag

def update_bag(bag_id: int, data: dict) -> Bag:
    bag = get_bag_by_id(bag_id)
    for key, value in data.items():
        setattr(bag, key, value)
    db.session.commit()
    return bag

def delete_bag(bag_id: int) -> None:
    bag = get_bag_by_id(bag_id)
    db.session.delete(bag)
    db.session.commit()