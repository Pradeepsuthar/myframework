"""Main Project File"""
from lib import settings as ps
from lib import project as project
import sys
import os
import datetime

now = datetime.datetime.now()

set_obj = ps.Settings()
set_obj.allSettings()
myproject = project.Project()
args_list = sys.argv
current_file = args_list[0]
slice_object = slice(-1, -10, -1)
py_file = current_file[slice_object][::-1]

def main():
    '''root file'''
    print("="*100)
    args = sys.argv
    try:
        if sys.argv[1] == 'createproject':
            project_name = args[2]
            myproject.create(project_name)
        elif sys.argv[1] == 'startproject':
            string = '''Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
%s
'''%(now.strftime("%B %d, %Y - %H:%M:%S"))
            print(string)
        elif py_file == 'manage.py':
            cmd_error()
        else:
            cmd_error()
    except IndexError as error:
        cmd_error()
        
def cmd_error():
    '''Output expected IndexErrors.'''
    print("\nType '%s help <subcommand>' for help on a specific subcommand." % py_file)
    print("\nAvailable subcommands:\n")
    subcommands = ['createproject', 'startproject']
    for i in subcommands:
        print("->", i)

if __name__ == '__main__':
    main()
