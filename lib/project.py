import os

class Project:
    def create(self, project_name):
        try:
            os.mkdir(project_name)
            # Create target Directory
            project_files = ['views.py','urls.py','app.py']
            current_dir_path = os.getcwd()+"\\"+project_name   
            print("\n%s, your project is created"%(project_name))
            for i in range(len(project_files)):
                abs_file_path = os.path.join(current_dir_path, project_files[i])
                open(abs_file_path,"x")
        except FileExistsError:
            print("\n%s, your project is already exists"%(project_name))
            








            