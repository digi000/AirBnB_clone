#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def emptyline(self):
        pass

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True
    
    def do_EOF(self, arg):
        '''Exit the program when EOF (Ctrl+D) is reached'''
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()