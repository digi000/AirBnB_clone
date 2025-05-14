#!/usr/bin/env python3
"""py shell"""
import cmd, json, os
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """class shell"""
    prompt = "(hbnb) "
    clas = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity, 'City': City, 'Place': Place, 'Review': Review}
    def do_quit(self, line):
        """quit"""
        return True
    def do_EOF(self, line):
        """ctrl+D"""
        return True
    def emptyline(self):
        pass
    def do_create(self, line):
        if line in self.clas:
            i1 = self.clas[line]()
            i1.save()
            print(i1.id)
        elif line == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
    
    def do_show (self, line):
        if len(line.split()) == 0:
            print("** class name missing **")
        elif line.split()[0] not in  self.clas:
            print("** class doesn't exist **")
        elif len(line.split()) == 1:
            print("** instance id missing **")
        else:
            line1 = line.replace(' ', '.')
            if os.path.exists("file.json"):
                with open("file.json", 'r') as f:
                    text = f.read()
                    if text:
                        objs = json.loads(text)
                        if line1 in objs:
                            vl = objs[line1]
                            df = self.clas[line.split()[0]](**vl)
                            print(df)
                        else:
                            print("** no instance found **")
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Useage: destroy <class name> <id>"""
        if len(line.split()) == 0:
            print("** class name missing **")
        elif line.split()[0] not in self.clas:
            print("** class doesn't exist **")
        elif len(line.split()) == 1:
            print("** instance id missing **")
        else:
            line1 = line.replace(' ', '.')
            with open("file.json", 'r') as f:
                text = f.read()
                if text:
                    objs = json.loads(text)
                    if line1 in objs:
                        del objs[line1]
                        with open("file.json", 'w') as f:
                            f.write(json.dumps(objs))
                    else:
                        print("** no instance found **")

    def do_all(self, line):
        if line == "" or line in self.clas:
            with open("file.json", 'r') as f:
                text = f.read()
                if text:
                    objs = json.loads(text)
                    if objs:
                        ty = []
                        for key, value in objs.items():
                            my_model = self.clas[key.split('.')[0]](**value)
                            ty.append(my_model.__str__())
                        print(ty)
        else:
            print("** class doesn't exist **")
    def do_update(self, line):
        if len(line.split()) == 0:
            print("** class name missing **")
        elif line.split()[0] not in self.clas:
            print("** class doesn't exist **")
        elif len(line.split()) == 1 and line.split()[0] in self.clas:
            print("** instance id missing **")
        else:
            ds = line.split()
            line1 = ds[0]+'.'+ds[1]
            with open("file.json", 'r') as f:
                text = f.read()
                if text:
                    objs = json.loads(text)
                    if line1 in objs:
                        if len(line.split()) < 3:
                            print("** attribute name missing **")
                        else:
                            if line.split()[2] in objs[line1]:
                                if len(line.split()) < 4:
                                    print("** value missing **")
                                else:
                                    objs[line1][line.split()[2]] = line.split()[3]
                        with open("file.json", 'w') as f:
                            f.write(json.dumps(objs))
                    else:
                        print("** no instance found **")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
