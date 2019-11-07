#!/usr/bin/python3
"""Module Base Model"""

import uuid
import datetime


class BaseModel:
    """Class BaseModel"""

    def __init__(self):
        """Constructor"""
        self.id = str(uuid.uuid4())

