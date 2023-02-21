#!/usr/bin/python3
"""Console"""
import cmd
import models


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
        if not arg:
            print("** class name missing **")
            return

        if arg not in models.CLS_NAMES:
            print("** class doesn't exist **")
            return
        cls = models.CLS_NAMES[arg]
        instance = cls()
        """ Save the instance to the JSON file """
        models.storage.save()
        print(instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
