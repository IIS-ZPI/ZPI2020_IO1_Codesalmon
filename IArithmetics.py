from abc import ABC, abstractmethod

class IArithmetics(ABC):
    @abstractmethod
    @staticmethod
    def Addition(a, b):
        pass

    @abstractmethod
    @staticmethod
    def Difference(a, b):
        pass

    @abstractmethod
    @staticmethod
    def Division(a, b):
        # Komentarz
        pass

    @abstractmethod
    @staticmethod
    def Multiply(a, b):
        pass
