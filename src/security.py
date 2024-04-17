from abc import ABC, abstractmethod

class Security(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def set_password(self):
        pass