from abc import ABC, abstractmethod

class IArithmetics(ABC):
    @abstractmethod
    @staticmethod
    def Addition(a, b):
        pass

    @abstractmethod
    @staticmethod
    def Difference():
        pass

    @abstractmethod
    @staticmethod
    def Division():
        pass

    @abstractmethod
    @staticmethod
    def Multiply():
        pass
