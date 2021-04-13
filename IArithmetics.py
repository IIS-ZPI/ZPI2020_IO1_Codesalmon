from abc import ABC, abstractmethod

class IArithmetics(ABC):
    @abstractmethod
    @staticmethod
    def Addition(a, b):
        pass

    @abstractmethod
    @staticmethod
    def Difference(a, b):
        return a-b

    @abstractmethod
    @staticmethod
    def Division(a, b):
        pass

    @abstractmethod
    @staticmethod
    def Multiply(a, b):
		return a * b
        pass
