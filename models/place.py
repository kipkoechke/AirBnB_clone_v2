#!/usr/bin/python3
"""Defines the Place class."""

from models.base_model import BaseModel

class Place(BaseModel):
    """Represents a place.

    Attributes:
        city_id (str): City id.
        user_id (str): User id.
        name (str): Place name.
        description (str): Place description.
        number_rooms (int): Number of rooms.
        number_bathrooms (int): Number of bathrooms.
        max_guest (int): Maximum number of guests.
        price_by_night (int): Price per night.
        latitude (float): Latitude coordinates.
        longitude (float): Longitude coordinates.
        amenity_ids (list): List of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

