#!/usr/bin/python3
"""Console"""
import cmd
import json

from models.base_model import BaseModel



class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb) '
    classes = {"BaseModel"}

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
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name != BaseModel:
            print("** class doesn't exist **")
            return
        cls = BaseModel()
        cls.save()
        print(cls.id)
    
    def do_show(self, arg):
        """" Prints string representation of an instance """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")

    def do_destroy(self, arg):
        pass

    def do_all(self, arg):
        pass

    def do_update(self, arg):
        pass





if __name__ == '__main__':
    HBNBCommand().cmdloop()
