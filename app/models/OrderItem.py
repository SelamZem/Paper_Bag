from . import db

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    bag_id = db.Column(db.Integer, db.ForeignKey('bags.id'), nullable=False)

    # Relationship
    bag = db.relationship('Bag', back_populates='order_items')

    @property
    def total_price(self):
        return self.bag.price * self.quantity

    def __repr__(self):
        return f'<OrderItem {self.id} - Bag {self.bag_id}>'
