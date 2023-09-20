#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 nullable=False, primary_key=True),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"), nullable=False,
                                 primary_key=True))

    @property
    def reviews(self):
        """[reviews getter]

        Returns:
            [list]: [list of review instances]
        """
        reviews_list = []
        for revs in models.storage.all(Review).values():
            if reviews.place_id == self.id:
                reviews_list.append(revs)
        return reviews_list

    @property
    def amenities(self):
        """[amenities getter]

        Returns:
            [list]: [list of Amenities]
        """
        import models
        from models.amenity import Amenity
        amenities_list = []
        for ams in models.storage.all(Amenity).values():
            if ams.id in ams.id:
                amenities_list.append(ams)
        return amenities_list

    @amenities.setter
    def amenities(self, val):
        """[amenities setter]

        Args:
            val ([obj]): [obj to be set]
        """
        if isinstance(self, val, Amenity):
            self.amenity_ids.append(val.id)
