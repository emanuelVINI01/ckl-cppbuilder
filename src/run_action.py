from actions import Action
from build_action import BuildAction
import os   
class RunAction (Action):
    def __init__(self) -> None:
        super().__init__("run")
        self.build_action = BuildAction()
    def run(self, args : list[str]):
        output = self.build_action.run(args)
        _ = os.system('clear' if os.name == 'posix' else 'cls')
        os.system(output)