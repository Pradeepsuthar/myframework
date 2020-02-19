"""Main Project File"""
from lib import settings as ps
from lib import project as project
import sys
import os

def main():
    set_obj = ps.Settings()
    set_obj.allSettings()

    myproject = project.Project()

    args_list = sys.argv

    current_file = args_list[0]
    slice_object = slice(-1, -10, -1)

    py_file = current_file[slice_object][::-1]
    print("="*100)

    args = sys.argv

    for cmd in args:
        if cmd == 'createproject' or cmd == args_list[0]:
            try:
                project_name = args[2]
                myproject.create(project_name)
                break
            except IndexError as error:
               
                print("\nType '%s help <subcommand>' for help on a specific subcommand."%py_file)
                cmd_error()
                break


def cmd_error():
    '''Output expected IndexErrors.'''
    print("\nAvailable subcommands:\n")
    subcommands = ['createproject','startproject']
    for i in subcommands:
        print("->",i)

if __name__ == '__main__':
    main()