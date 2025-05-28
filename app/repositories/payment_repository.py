from typing import List
from flask import abort
from app.models import db
from app.models.Payment import Payment, PaymentStatus

def list_payments() -> List[Payment]:
    return Payment.query.all()

def get_payment_by_id(payment_id: int) -> Payment:
    payment = Payment.query.get(payment_id)
    if not payment:
        abort(404, f"Payment {payment_id} not found")
    return payment

def list_payments_by_order(order_id: int) -> List[Payment]:
    return Payment.query.filter_by(order_id=order_id).all()

def list_payments_by_status(status: str) -> List[Payment]:
    return Payment.query.filter_by(status=status).all()

def create_payment(data: dict) -> Payment:
    payment = Payment(**data)
    db.session.add(payment)
    db.session.commit()
    return payment

def update_payment(payment_id: int, data: dict) -> Payment:
    payment = get_payment_by_id(payment_id)
    for key, value in data.items():
        setattr(payment, key, value)
    db.session.commit()
    return payment

def delete_payment(payment_id: int) -> None:
    payment = get_payment_by_id(payment_id)
    db.session.delete(payment)
    db.session.commit()