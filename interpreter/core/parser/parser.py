import os
import sys

sys.path.append(os.getcwd())

from interpreter.core.language_constructs.containers.containers import *
from interpreter.core.language_constructs.data_types.data_types import *
from interpreter.core.language_constructs.functions.functions import *
from interpreter.core.language_constructs.objects.object_types import *
from interpreter.interpreter import Program
from interpreter.core.symbol_table.symbol_table import VariableNameFactory

class Parser:
    # Static Parser
    def separate(target):
        result = []
        current_str, scope_depth = '', 0
        is_in_quotes = False
        for symb in target:
            if scope_depth == 0 and symb == ' ' and is_in_quotes == False:
                if len(current_str) > 0:
                    result.append(current_str)
                current_str = ''
            else:
                match symb:
                    case '(': scope_depth += 1
                    case ')': scope_depth -= 1
                    case '"': is_in_quotes = not is_in_quotes
                current_str = current_str + symb
        if len(current_str) > 0:
            result.append(current_str)
        return result
    
    def parseFunctionCall(program, function_call: str):
        if function_call[0] != '(':
            raise RuntimeError("Internal error, incorrect command format!")
        parsed_function_call =  Parser.separate(function_call[1:len(function_call)-1])
        function, args = parsed_function_call[0], parsed_function_call[1:]
        return function, args
        
    def parseExpression(expression: str, program):
        if len(expression) == 0:
            program.logger.raiseError()
        elif expression[0] == '(':
            instruction, args = Parser.parseCommand(program, expression)
            return (FunctionFactory.createFunction(instruction), args)
        elif expression[0] == '\"':
            return ValueFactory.createString(expression[1:len(expression)-1])
        elif expression == "true" or expression == "false":
            return ValueFactory.createBoolean(expression == "true")
        elif expression == "null":
            return ValueFactory.createNull()
        elif ord('a') <= ord(expression[0]) and ord(expression[0]) <= ord('z'):
            return VariableNameFactory.createVariabaleName(expression)
        elif '.' in expression:
            return ValueFactory.createFloat(float(expression))
        else:
            return ValueFactory.createInt(int(expression))