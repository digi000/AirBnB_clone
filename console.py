#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def emptyline(self):
        pass

    def do_quit(self, args):
        '''Quit command to exit the program'''
        return True
    
    def do_EOF(self, args):
        '''Exit the program when EOF (Ctrl+D) is reached'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()