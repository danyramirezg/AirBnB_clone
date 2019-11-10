#!/usr/bin/python3
"""Program console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class that displays the console"""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Command to exit the program"""
        return True

    def do_EOF(self):
        """Command on console (CTRL + D)"""
        return True

    def emptyline(self):
        """An empty line doesn't execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
