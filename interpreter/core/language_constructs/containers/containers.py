import os
import sys

sys.path.append(os.getcwd())

from interpreter.core.language_constructs.objects.object_types import Constant
from interpreter.core.language_constructs.data_types.data_types import ValueFactory, Numerical

from abc import ABC, abstractmethod


class Container(ABC):

    @abstractmethod
    def __init__(self, elements):
        pass


class ListNumerical(Container): # Maybe create an abstract list class that accepts data type (?)

    def __init__(self, elements):
        for element in elements:
            if not isinstance(element, Numerical):
                raise RuntimeError("Non numerical data in the numerical list.")
        self.__list = elements
    
    def getSum(self,):
        result = Constant(ValueFactory.createInt(0))
        for element in self.__list:
            result = result + element
        return result   
    
    def getProduct(self,):
        result = Constant(ValueFactory.createInt(1))
        for element in self.__list:
            result = result * element
        return result   
    
    def max(self,):
        result = Constant(ValueFactory.createInt(self.__list[0] - 1)) # Value that is less than maximum to reassign with correct datatype 
        for element in self.list:
            result = result.max(element)
        return result

    def min(self,):
        result = Constant(ValueFactory.createInt(self.__list[0] + 1)) # Value that is bigger than minimum to reassign with correct datatype 
        for element in self.list:
            result = result.min(element)
        return result
 
    def debugPrint(self,):
        for element in self.list:
            print(element.getValue().value)


class ContainerFactory:

    def createList(list) -> ListNumerical:
        return ListNumerical(list)