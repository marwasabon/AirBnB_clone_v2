#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(
        String(128),
        nullable=False
    )
    cities = relationship('City', back_populates='state')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def get_cities(self):
            obj = models.storage.all(City)
            ls = [v for k, v in obj.items() if v.state_id == self.id]
            sorted(ls, key=lambda city: city.name)
            return ls
