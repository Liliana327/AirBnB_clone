#!/usr/bin/python
""" holds class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwars):
        """initializes"""
        super().__init__(*args, **kwargs)
