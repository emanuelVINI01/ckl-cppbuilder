import sys
from build_action import BuildAction
from init_action import InitAction
from run_action import RunAction

actions = [
    InitAction(),
    BuildAction(),
    RunAction()
]
process_args = sys.argv[1:]
if len(process_args) == 0:
    print("Please provide a argument to run CKL")
else:
    action_name = process_args[0]
    args = process_args[1:]
    for action in actions:
        if action.name == action_name:
            action.run(args)
            exit(0)
    print("None action found with this name")