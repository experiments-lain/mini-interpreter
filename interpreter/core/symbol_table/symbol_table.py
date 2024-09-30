import os
import sys
sys.path.append(os.getcwd())

from interpreter.core.language_constructs.data_types.data_types import *
from interpreter.core.language_constructs.objects.object_types import *
from interpreter.interpreter import Program


class VariableName:
    
    def __init__(self, variable_name):
        self.variable_name = variable_name
    
    def getName(self,) -> str:
        return self.variable_name
    
    def __hash__(self,):
        return hash(self.variable_name)
        


class VariableNameFactory:

    @staticmethod
    def isValidName(name) -> bool:
        def isAllowedSymbol(symb) -> bool:
            if ord('a') <= ord(symb) and ord(symb) <= ord('z'):
                return True
            if ord('A') <= ord(symb) and ord(symb) <= ord('Z'):
                return True
            if ord('0') <= ord(symb) and ord(symb) <= ord('9'):
                return True
            return False
        if len(name) == 0 or (ord('a') <= name[0] and name[0] <= ord('z')):
            return False
        for symbol in name:
            if not isAllowedSymbol(symbol):
                return False
        return True

    def createVariableName(name: str, program: Program) -> VariableName:
        if not VariableNameFactory.isValidName(name):
            program.raiseError()
        return VariableName(name)


class SymbolTable:
    def __init__(self, program):
        self.variables = {}
        self.src_program = program
 
    def addVar(self, variable_name: VariableName, value: Value):
        # value is in value type class form 
        if variable_name in self.variables:
            self.src_program.logger.raiseError()
        self.variables.update({variable_name : ObjectFactory.createVariable(variable_name, value)})
    
    def getVar(self, variable_name):
        if not (variable_name in self.variables):
            self.src_program.logger.raiseError()
        return self.variables[variable_name]