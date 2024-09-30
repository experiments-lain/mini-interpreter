import os
import sys
sys.path.append(os.getcwd())

from interpreter.utils.logger.logger import Logger
from interpreter.core.symbol_table.symbol_table import SymbolTable
from interpreter.core.language_constructs.functions.functions import Function
from interpreter.core.parser.parser import Parser

class Program:
    def __init__(self, target_code: list[str]):
        self.logger = Logger(self)
        self.storage = SymbolTable(self)
        self.target_code = target_code
        self.current_line = 0
 
    def moveToNextLine(self,):
        self.current_line += 1
        self.logger.current_line = self.current_line + 1
        if self.current_line == len(self.target_code):
            return False
        return True
 
    def execCurrentLine(self,):
        function, arguments = Parser.parseExpression(self.target_code[self.current_line], self)
        xxx = function.execute(arguments)
        if not self.moveToNextLine():
            self.terminate()
 
    def terminate(self,):
        # SEND OUTPUT FROM self.logger.output
        for line in self.logger.output:
            print(line)
        quit()