#!/usr/bin/env python3
"""user"""
from .base_model import BaseModel
class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self, *args, **kwargs):
        """initializer"""
        super().__init__(*args, **kwargs)