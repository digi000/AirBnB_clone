#!/usr/bin/env python3
"""3. BaseModel"""
import uuid
from datetime import datetime
class BaseModel:
    """3. BaseModel"""
    def __init__(self, *args, **kwargs):
        """intializer"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "created_at" and key != "updated_at":
                    if key[0] != '_':
                        setattr(self, key, value)
                else:
                    self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from . import storage
            storage.new(self)

    def __str__(self):
        """string representation"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """upadetes at updated at"""
        self.updated_at = datetime.now()
        from . import storage
        storage.save()

    def to_dict(self):
        """returns a dictionary"""
        dr = self.__dict__.copy()
        dr["__class__"] = f"{type(self).__name__}"
        dr["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dr["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dr