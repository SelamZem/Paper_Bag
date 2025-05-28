from typing import List
from flask import abort
from app.models import db
from app.models.Category import Category
from app.models.Bag      import Bag


CATEGORY_MAP = {
    "small": 1,
    "medium1": 2,
    "medium2": 3,
    "large": 4
}

def list_categories() -> List[Category]:
    return Category.query.all()

def get_category_by_id(category_id: int) -> Category:
    cat = Category.query.get(category_id)
    if not cat:
        abort(404, f"Category {category_id} not found")
    return cat

def list_bags_for_category(category_id: int) -> List[Bag]:
    return Bag.query.filter_by(category_id=category_id).all()


def create_category(data: dict) -> Category:
    name = data.get("name")
    if name not in CATEGORY_MAP:
        raise ValueError("Invalid category name. Must be one of: small, medium1, medium2, large.")
    
    data["id"] = CATEGORY_MAP[name]  
    cat = Category(**data)
    db.session.add(cat)
    db.session.commit()
    return cat

def update_category(category_id: int, data: dict) -> Category:
    name = data.get("name")
    if name and name not in CATEGORY_MAP:
        raise ValueError("Invalid category name. Must be one of: small, medium1, medium2, large.")
    
    cat = get_category_by_id(category_id)
    
    for key, value in data.items():
        setattr(cat, key, value)
    
    if name:
        cat.id = CATEGORY_MAP[name]  # Update ID based on name

    db.session.commit()
    return cat


def delete_category(category_id: int) -> None:
    cat = get_category_by_id(category_id)
    db.session.delete(cat)
    db.session.commit()