import uuid
import datetime

class BaseModel:
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        return {
                "my_number":self.my_number,
                "name":self.name,
                "__class__":__class__.__name__,
                "updated_at":self.updated_at.isoformat(),
                "id":self.id,
                "created_at":self.created_at.isoformat()
                }
