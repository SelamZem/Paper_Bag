from . import db

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    
    #Relationship
    bags = db.relationship('Bag', backref='category', lazy=True)
    
    def __repr__(self):
        return f'<Category {self.name}>' 