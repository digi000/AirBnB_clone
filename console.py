#!/usr/bin/env python3
"""py shell"""
import cmd
class HBNBCommand(cmd.Cmd):
    """class shell"""
    prompt = "(hbnb) "
    def do_quit(self, line):
        """quit"""
        return True
    def do_EOF(self, line):
        """ctrl+D"""
        return True
    def emptyline(self):
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
