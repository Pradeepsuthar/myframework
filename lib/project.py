import os

class Project:
    def create(self, project_name):
        print("%s, your project is created"%(project_name))
        project_file = project_name+".py"


        
        dirName = 'src'
 
        try:
            # Create target Directory
            script_dir = os.path.dirname(__file__)
            abs_file_path = os.path.join(script_dir, project_file)
            print(abs_file_path)
            open(abs_file_path,"x")
            os.mkdir(dirName)
            print("Directory " , dirName ,  " Created ") 
        except FileExistsError:
            print("Directory " , dirName ,  " already exists")
            