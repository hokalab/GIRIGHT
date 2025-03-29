from . import db

class Gear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100))
    weight = db.Column(db.Float, nullable=False)  # g単位
    category = db.Column(db.String(50))
    essential = db.Column(db.Boolean, default=True)
    notes = db.Column(db.Text)
    is_packed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Gear {self.name} - {self.weight}g>"