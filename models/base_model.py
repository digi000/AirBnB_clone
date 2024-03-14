import uuid
import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for ky, vl in kwargs.items():
                if ky != "__class__":
                    if ky == 'created_at' or ky == 'updated_at':
                        df = '%Y-%m-%dT%H:%M:%S.%f'
                        vl = datetime.datetime.strptime(vl, df)
                    setattr(self, ky, vl)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        self.__dict__['__class__'] = __class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__
