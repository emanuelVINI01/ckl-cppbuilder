from actions import Action
from project import project_name, os_extension
import yaml
import os   
import glob
class BuildAction (Action):
    def __init__(self) -> None:
        super().__init__("build")

    def run(self, _: list[str]) -> dict:
        try:
            name = project_name()
            print(f"Starting build of project {name}...")
            build = yaml.safe_load(
                open("./build.ckl.yaml")
            )
            includes = []
            for include in build["includes"]:
                includes.append(f"-I {include}")
            files = []
            for directory in build["source"]["directories"]:
                for path in glob.glob(directory, recursive=True):
                    if os.path.isfile(path):
                        print (str(path))
                        if not str(path) in build["source"]["excludes"]:
                            files.append(path)

            output_file = build['output']['file'].replace(
                '${exec_type}', os_extension())
            output_dir = build['output']['directory']
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            cmd = f"{build['compiler']} {' '.join(files)} {' '.join(includes)} {' '.join(build['extra_arguments'])} -o {output_dir}{os.path.sep}{output_file}"
            print(f"Running build with command: {cmd}")
            out = os.system(cmd)
            if out == 0:
                print("Build successfully")
            else:
                print("Fail while building, check console above")
                exit(-1)
            return output_dir + os.path.sep + output_file
        except Exception as e:
            print(e)
            print("Project properties not found")
