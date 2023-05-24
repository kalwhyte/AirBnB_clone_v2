#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table amenities.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
<<<<<<< HEAD
    # place_amenities = relationship("Place", secondary="place_amenity", viewonly=False, overlaps="place_amenities")
=======
    #place_amenities = relationship("Place", secondary="place_amenity",
				#viewonly=False, overlaps="place_amenities")
>>>>>>> 7e84b8d77bfaf2ea8b7630ba7ac3e39e93694429
