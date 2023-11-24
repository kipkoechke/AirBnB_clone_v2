#!/usr/bin/python3
"""Defines the City class."""

from models.base_model import BaseModel

class City(BaseModel):
    """Represents a city.

    Attributes:
        state_id (str): State id.
        name (str): City name.
    """

    state_id = ""
    name = ""

