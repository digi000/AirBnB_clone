import json
import uuid
import datetime
#from .. import base_model

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        ky = f'{obj.__class__.__name__}.{obj.__dict__.get("id")}'
        self.__objects[ky] = obj.to_dict()
         
        '''
        for kh, vl in pd.items():
            if isinstance(vl, datetime.datetime):
                pd[kh] = str(vl.isoformat())
        self.__objects[ky] = pd
        '''

        objg = obj.to_dict()
        for rt in objg.keys():
            print(type(objg[rt]))
        print(f"{objg}")

        print(f"my pd = {self.__objects}")

    def save(self):
        json_str = json.dumps(self.__objects)

        with open(self.__file_path, 'w') as jsfile:
            jsfile.write(json_str)

    def reload(self):
        try:
            with open (self.__file_path, 'r') as jsfile:
                json_str = jsfile.read()
                self.__objects = json.loads(json_str)
        except Exception:
            pass
