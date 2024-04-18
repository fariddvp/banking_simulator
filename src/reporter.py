from abc import ABC, abstractmethod

class Reporter(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def show_details(self):
        pass