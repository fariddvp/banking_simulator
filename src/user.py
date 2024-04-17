from abc import ABC

class User(ABC):
    def __init__(self,nationality_code, first_name, last_name) -> None:
        self.nationality_code = nationality_code
        self.first_name = first_name
        self.last_name = last_name

        