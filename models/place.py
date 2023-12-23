#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    #city = relationship('City', back_populates='places')
    '''
    #city_id = ""
    #user_id = ""
    #name = ""
    #description = ""
    #number_rooms = 0
    #number_bathrooms = 0
    #max_guest = 0
    #price_by_night = 0
    #latitude = 0.0
    #longitude = 0.0
    #amenity_ids = []
    '''
    '''
    @property
    def reviews(self):
        returns the list of review instances with
        place_id equal the current place.id
        cur_id = self.id
        review_list = []
        objs = storage.all('Review')
        for k, v in obj.items():
            if v.place_id == cur_id:
                review_list.append(str(v))
        return (review_list)
        '''
    reviews = relationship('Review', back_populates='place')
