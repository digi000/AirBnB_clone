#!/usr/bin/env python3
"""3. BaseModel"""
import uuid
from datetime import datetime
class BaseModel:
    """3. BaseModel"""
    def __init__(self, *args, **kwargs):
        """intializer"""
        if kwargs:
            self.id = kwargs["id"]
            self.my_number = kwargs["my_number"]
            self.name = kwargs["name"]
            self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """string representation"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """upadetes at updated at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary"""
        dr = self.__dict__
        dr["__class__"] = f"{type(self).__name__}"
        dr["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dr["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dr
