#!/usr/bin/python3
"""Console for holbertonschool-AirBnB_clone"""


import cmd
import sys
import models
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """
    our cmd loop interpreter
    """
    intro = 'Welcome to the shell. Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, args):
        """Quit console at EOF\n"""
        print("")
        return True

    def do_create(self, arg):
        """sd  f df df  df """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.class_names:
            print("** class doesn't exist **")
        else:
            cr_inst = BaseModel()
            cr_inst.save()
            print(cr_inst.id)

    def do_show(self, arg):
        """sdsdsd s d sdsa dsd """
        arg_list = arg.split(" ")
        if len(arg_list) < 1:
            print("** class name missing **")
        elif arg_list[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instnace id missing **")
        else:
            stored_objs = storage.all()
            if f"{arg_list[0]}.{arg_list[1]}" in stored_objs.keys():
                print(f"{stored_objs[f'{arg_list[0]}.{arg_list[1]}']}")
            else:
                print("** no instance found **")

    def emptyline(self):
        """No action: input is empty line + ENTER\n"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id\n"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if len(arg) > 1:
                raise TypeError("Incorrect number of arguments")
        if args in classess:
            instance = eval(str(args) + "()")
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")
            return False

    def do_show(self, args):
        """Prints the string representation of an instance\n"""
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if len(arg) == 1:
            raise TypeError("Incorrect number of arguments")
            return False
        if len(arg[1]) == 0:
            print("** instance id missing **")
            return False
        if len(arg) > 2:
            raise TypeError("Incorrect number of arguments")
            return False
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return False
        else:
            key = arg[0] + "." + arg[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id\n"""
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if len(arg) == 1:
            raise TypeError("Incorrect number of arguments")
            return False
        if len(arg[1]) == 0:
            print("** instance id missing **")
            return False
        if len(arg) > 2:
            raise TypeError("Incorrect number of arguments")
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return False
        else:
            key = arg[0] + "." + arg[1]
            if key in models.storage.all():
                del(models.storage.all()[key])
                models.storage.save
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        Based or not on the class name\n"""
        arg = args.split()
        objList = []
        if len(args) == 0:
            for key in models.storage.all():
                objList.append(str(models.storage.all()[key]))
            print(objList)
        if len(arg) == 1:
            if arg[0] in classes:
                for key in models.storage.all():
                    if arg[0] in key:
                        objList.append(str(models.storage.all()[key]))
                print(objList)
            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance
        Based on class name and id
        By adding or updating attribute"""
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if len(arg) == 2:
            print("** attribute name missing **")
            return False
        if len(arg) == 3:
            print("** value missing **")
            return False
        if len(arg) > 4:
            raise TypeError("Incorrect number of arguments")
            return False
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return False
        else:
            key = arg[0] + "." + arg[1]
            if key in models.storage.all():
                setattr(models.storage.all()[key], arg[2], arg[3])
                models.storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    """our main"""
    HBNBCommand().cmdloop()
