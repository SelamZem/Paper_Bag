from . import db

class CartItem(db.Model):
    __tablename__ = 'cart_items'
    
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    bag_id = db.Column(db.Integer, db.ForeignKey('bags.id'), nullable=False)

    bag = db.relationship('Bag')
    
    def __repr__(self):
        return f'<CartItem {self.id}>' 
    
    @property
    def total_price(self):
        return self.bag.price * self.quantity

 