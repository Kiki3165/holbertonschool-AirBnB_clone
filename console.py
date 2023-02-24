#!/usr/bin/python3
"""Console"""
import cmd
import json

from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.base_model import BaseModel
from models import storage



class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb) '
    classes = {"BaseModel", "User", "Amenity", "City", "Review", "State", "Place"}

    def do_quit(self, line):
        """Quit command"""
        return True

    def do_EOF(self, line):
        """EOF command"""
        return True

    def emptyline(self):
        """Do nothing if empty line"""
        pass

    def do_create(self, arg):
        """ Create new instance of BaseModel """
        if not arg:
            print('** class name missing **')
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        '''Prints the string representation of an instance based on the class name and id'''
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
        else:
            obj = all_objs[key]
            print(obj)

    def do_destroy(self, arg):
        """Destroy command to delete an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
        else:
            del all_objs[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        if arg:
            try:
                cls = eval(arg)
                all_objs = storage.all(cls)
                print([str(all_objs[obj]) for obj in all_objs])
            except:
                print("** class doesn't exist **")
                return
            else:
                all_objs = storage.all()
                print([str(all_objs[obj]) for obj in all_objs])

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = all_objs[key]
        attr_name = args[2]
        value = args[3]

        """ Cast the attribute value to its corresponding data type """
        if isinstance(obj.__dict__[attr_name], int):
            value = int(value)
        elif isinstance(obj.__dict__[attr_name], float):
            value = float(value)
        else:
            value = str(value)

        setattr(obj, attr_name, value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
