import uuid
import datetime

class BaseModel:
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.now().isoformat())
        self.updated_at = str(datetime.datetime.now().isoformat())

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = str(datetime.datetime.now().isoformat())

    def to_dict(self):
        return self.__dict__
