#!/usr/bin/python3
""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    ""

    prompt = '(hbnb) '
    cls_names = ['BaseModel', 'User', 'State', 'City',
                 'Amenity', 'Place', 'Review']

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        "EOF command to exit the program"
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        ""
        if self.validate_input(line):
            classes = {'BaseModel': BaseModel,
                       'User': User,
                       'State': State,
                       'City': City,
                       'Amenity': Amenity,
                       'Place': Place,
                       'Review': Review}

            obj = classes[line]()
            storage.save()
            print(obj.id)

    def do_show(self, line):
        ""
        if self.validate_input(line, True):
            args = line.split()
            print(storage.all()[args[0] + '.' + args[1]])

    def do_destroy(self, line):
        ""
        if self.validate_input(line, True):
            args = line.split()
            del storage.all()[args[0] + '.' + args[1]]
            storage.save()

    def do_all(self, line):
        ""
        lenght = len(line.split())
        if lenght == 1 and line not in self.cls_names:
            print("** class doesn't exist **")
            return
        objs = []
        for k, v in storage.all().items():
            if line in k:
                objs.append(str(v))
        if objs:
            print(objs)

    def do_update(self, line):
        ""
        if self.validate_input(line, True, True):
            args = line.split()
            obj = storage.all()[args[0] + '.' + args[1]]
            setattr(obj, args[2], str(args[3])[1:-1])
            obj.save()

    def validate_input(self, line, has_id=False, has_attr=False):
        args = line.split()
        lenght = len(args)
        if lenght == 0:
            print('** class name missing **')
            return False
        elif args[0] not in self.cls_names:
            print("** class doesn't exist **")
            return False
        elif has_id and lenght == 1:
            print('** instance id missing **')
            return False
        elif has_id and args[0] + '.' + args[1] not in storage.all():
            print('** no instance found **')
            return False
        elif has_attr and lenght == 2:
            print('** attribute name missing **')
            return False
        elif has_attr and lenght == 3:
            print('** value missing **')
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
