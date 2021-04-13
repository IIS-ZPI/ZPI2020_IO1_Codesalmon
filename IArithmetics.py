from abc import ABC, abstractmethod

class IArithmetics(ABC):
    @abstractmethod
    @staticmethod
    def Addition(a, b):
        # Komentarz 1
        pass

    @abstractmethod
    @staticmethod
    def Difference(a, b):
        # Komentarz 2
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
