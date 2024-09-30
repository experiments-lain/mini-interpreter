import os
import sys
sys.path.append(os.getcwd())

from interpreter.core.language_constructs.containers.containers import *
from interpreter.core.language_constructs.data_types.data_types import *
from interpreter.core.language_constructs.objects.object_types import *
from interpreter.core.parser.parser import Parser
from interpreter.core.symbol_table.symbol_table import VariableName
from interpreter.standard_functions_library.standard_functions_library import FunctionsLibrary

class Arguments:

    def __init__(self, arg_types):
        self.arg_types = arg_types
    
    def validate(self, args, program):

        if len(self.arg_types) == 1 and self.arg_types[0] == ListNumerical:
            arg_types = [Numerical for _ in range(len(args))]
        else:
            arg_types = self.arg_types

        if len(args) != len(arg_types):
            program.raiseError()
        for type, arg in zip(arg_types, args):
            if isinstance(arg, VariableName):
                if not issubclass(type, VariableName) and not isinstance(program.symbol_table.getVar(arg).getValue(), type):
                    program.raiseError()
                if (not issubclass(type, Variable)) and not isinstance(arg.getValue(), type):
                    program.raiseError()
            elif not isinstance(arg, type):
                program.raiseError()

    def cast(self, args, program):
        self.validate(args, program)
        if len(self.arg_types) == 1 and self.arg_types[0] == ListNumerical:
            arg_types = [Numerical for _ in range(len(args))]
        else:
            arg_types = self.arg_types
        casted_args = []
        for type, arg in zip(arg_types, args):
            if isinstance(arg, VariableName) and issubclass(type, Value):
                casted_args.append(program.symbol_table.getVar(arg).getValue())
            elif isinstance(arg, VariableName) and issubclass(type, Variable):            
                casted_args.append(program.symbol_table.getVar(arg))
            else:                
                casted_args.append(arg)
        if len(self.arg_types) == 1 and self.arg_types[0] == ListNumerical:
            return ContainerFactory.createList(casted_args)
        return casted_args


class Function:


    def __init__(self, instruction, arguments_format, src_program):
        self.instruction = instruction
        self.args_format = arguments_format
        self.src_program = src_program
        self.functions_library = FunctionsLibrary(self.src_program)
    
    def eval_arguments(self, ):
        args = []
        for arg in self.arguments:
            parsed_arg = Parser.classify(arg, self.src_program)
            if len(parsed_arg) > 1:
                args.append(parsed_arg[0].execute(parsed_arg[1]))
            else:
                args.append(parsed_arg[0])
        args = self.args_format.cast(args, self.src_program)
        return args
    
    def execute(self, ):
        # Step 1 convert all arguments to Constant Values
        val_args = self.eval_arguments()
        # Step 2 execute
        self.functions_library.getattr(self.instruction)(*val_args)
            

class FunctionFactory:
    allowed_instructions = ['puts', 'set', 'concat', 'lowercase', 
        'uppercase', 'replace', 'substring', 'add', 'subtract', 
        'multiply', 'divide', 'abs', 'max', 'min', 'lt', 'gt',
        'equal', 'not_equal', 'str']
    
    instruction_args = {
        'puts' : Arguments([String]),
        'set' : Arguments([VariableName, Value]),
        'concat' : Arguments([String, String]),
        'lowercase' : Arguments([String]),
        'uppercase' : Arguments([String]),
        'replace' : Arguments([String, String, String]),
        'substring' : Arguments([String, Int, Int]),
        'add' : Arguments([ListNumerical]),
        'subtract' : Arguments([Numerical, Numerical]),
        'multiply' : Arguments([ListNumerical]),
        'divide' : Arguments([Numerical, Numerical]),
        'abs' : Arguments([Numerical]),
        'max' : Arguments([ListNumerical]),
        'min' : Arguments([ListNumerical]),
        'lt' : Arguments([Numerical, Numerical]),
        'gt' : Arguments([Numerical, Numerical]),
        'equal' : Arguments([Value, Value]),
        'not_equal' : Arguments([Value, Value]),
        'str' : Arguments([Value])
    }
        
    def createFunction(function_name, program) -> Function:
        if not function_name in FunctionFactory.allowed_instructions:
            program.raiseError()
        return Function(function_name, FunctionFactory.instruction_args[function_name], program)
