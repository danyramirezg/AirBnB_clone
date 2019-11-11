#!/usr/bin/python3
"""Review class"""

import models
from models.base_model import BaseModel


class State(BaseModel):
    """A class Review that inherits from BaseModel"""

    place_id = " "
    user_id = " "
    text = " "
