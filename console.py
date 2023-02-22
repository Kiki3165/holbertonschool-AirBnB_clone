#!/usr/bin/python3
"""Console"""
import cmd
import json

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage



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
        all_objs = FileStorage().all()
        if key not in all_objs:
            print("** no instance found **")
        else:
            print(all_objs[key])

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
        all_objs = FileStorage().all()
        if key not in all_objs:
            print("** no instance found **")
        else:
            del all_objs[key]
            FileStorage().save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
