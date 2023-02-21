#!/usr/bin/python3
"""Console"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb) '

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
