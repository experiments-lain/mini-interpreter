import sys
import os

sys.path.append(os.getcwd())

from interpreter.core.language_constructs.functions.functions import Function 
from interpreter.core.program_state.program_state_cl import ProgramState

class FunctionCall:
    
    def __init__(self, function: Function, args):
        self.function = function
        self.args = args

    def evalArguments(self, args, program_states: ProgramState):
        evaled_args = []
        for arg in args:
            if isinstance(arg, FunctionCall):
                evaled_args.append(arg.execute(program_states))
            else:
                evaled_args.append(arg)
        return evaled_args
    
    def execute(self, program_states: ProgramState):
        # Step 1 convert all arguments to Constant Values
        val_args = self.evalArguments(self.args, program_states)
        # Step 2 execute
        return self.function.execute(val_args, program_states)


class FunctionCallFactory:

    def createFunctionCall(function: Function, args):
        return FunctionCall(function, args)