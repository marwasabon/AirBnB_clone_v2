#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place",  secondary=Place.place_amenity, overlaps="amenities")

