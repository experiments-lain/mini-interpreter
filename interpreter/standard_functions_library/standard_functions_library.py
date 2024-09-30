import os
import sys
sys.path.append(os.getcwd())

from interpreter.core.language_constructs.containers.containers import *
from interpreter.core.language_constructs.data_types.data_types import *
from interpreter.core.language_constructs.objects.object_types import *
from interpreter.core.parser.parser import Parser
from interpreter.core.symbol_table.symbol_table import VariableName, VariableNameFactory
from interpreter.interpreter import Program


class FunctionsLibrary:
    
    def __init__(self, program: Program):
        self.src_program = program
    
    def puts(self, output: String):
        self.src_program.logger.print(output.getValue())
        return ValueFactory.createNull()
    
    def set(self, variable_name: VariableName, variable_value: Value):
        self.src_program.symbol_table.addVar(variable_name, variable_value)
        return ValueFactory.createNull()
    
    def concat(self, first: String, second: String):
        return first.concat(second)
    
    def lowercase(self, source: String):
        return source.lowercase()
    
    def uppercase(self, source: String):
        return source.uppercase()
    
    def replace(self, source: String, target: String, replacement: String):
        return source.replace(target, replacement)
    
    def substring(self, target_string: String, start: Int, end: Int):
        if start.min(end) < ValueFactory.createInt(0) or start.max(end) >= target_string.size():
            self.src_program.raiseError() 
        return target_string.substring(start, end)
    
    def add(self, list: ListNumerical):
        return list.getSum()
    
    def subtract(self, a: Numerical, b:Numerical):
        return a - b
    
    def multiply(self, list: ListNumerical):
        return list.getProduct()
    
    def divide(self, a: Numerical, b:Numerical):
        if b == ValueFactory.createInt(0):
            self.src_program.raiseError()
        return a / b
    
    def abs(self, a: Numerical):
        return a.abs()
    
    def max(self, list: ListNumerical):
        return list.max()
    
    def min(self, list: ListNumerical):
        return list.min()
    
    def lt(self, arg_1: Numerical, arg_2: Numerical):
        return arg_1 < arg_2
    
    def gt(self, arg_1: Numerical, arg_2: Numerical):
        return arg_1 > arg_2
    
    def equal(self, arg_1: Value, arg_2: Value):
        return arg_1 == arg_2
    
    def not_equal(self, arg_1: Value, arg_2: Value):
        return arg_1 != arg_2
    
    def str(self, arg):
        return arg.str()
    
    
    



