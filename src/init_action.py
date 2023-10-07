
from actions import Action
from project import project_name, os_extension
import shutil
import os   
class InitAction (Action):
    def __init__(self) -> None:
        super().__init__("init")

    def run(self, args: list[str]):
        if len(args) == 0:
            print("You need to provid the directory where project will be init")
        else:
            dir_name = args[0]
            if os.path.exists(dir_name):
                print(f"Directory {dir_name} already exists")
            else:
                shutil.copytree('./struct', dir_name)

                open(dir_name + os.path.sep + "ckl_properties.py",
                     "w").write(f"""name = \"{dir_name}\"
print("Loaded project properties")""")
                print("Project successfully init")
