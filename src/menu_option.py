from abc import ABC, abstractmethod

class MenuOption(ABC):
    @abstractmethod
    def execute(self):
        pass