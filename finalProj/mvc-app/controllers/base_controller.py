from abc import ABC, abstractmethod

class Controller(ABC):
    
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def update_display(self):
        pass