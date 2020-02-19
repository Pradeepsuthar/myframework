import os

class Project:
    def create(self, project_name):
        print("\n%s, your project is created"%(project_name))
        project_file = "views.py"
        
        try:
            os.mkdir(project_name)
            # Create target Directory
            script_dir = os.path.dirname(__file__)
            current_dir_path = os.getcwd()+"\\"+project_name
            abs_file_path = os.path.join(current_dir_path, project_file)
            open(abs_file_path,"x")
            print("Directory " , project_name ,  " Created ") 
        except FileExistsError:
            print("Directory " , project_name ,  " already exists")
            