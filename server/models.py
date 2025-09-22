from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# ------------------------
# Customer Model
# ------------------------
class Customer(db.Model, SerializerMixin):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # Relationships
    reviews = db.relationship("Review", back_populates="customer")

    # Association proxy (Task #2)
    items = association_proxy("reviews", "item")

    # Serialization (Task #3)
    serialize_rules = ("-reviews.customer",)


# ------------------------
# Item Model
# ------------------------
class Item(db.Model, SerializerMixin):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)

    # Relationships
    reviews = db.relationship("Review", back_populates="item")

    # Serialization (Task #3)
    serialize_rules = ("-reviews.item",)


# ------------------------
# Review Model
# ------------------------
class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)

    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))

    # Relationships
    customer = db.relationship("Customer", back_populates="reviews")
    item = db.relationship("Item", back_populates="reviews")

    # Serialization (Task #3)
    serialize_rules = ("-customer.reviews", "-item.reviews")


