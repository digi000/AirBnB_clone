import uuid
import json
import os


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        ky = f'{type(obj).__name__}.{id(self)}'
        self.__objects[ky]= obj

    def save(self):
        with open(self.__file_path, 'w') as json_file:
            json.dump(self.__objects,json_file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, obj_dict in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    cls = globals()[class_name]
                    obj_dict['created_at'] = datetime.strptime(obj_dict['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    obj_dict['updated_at'] = datetime.strptime(obj_dict['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
