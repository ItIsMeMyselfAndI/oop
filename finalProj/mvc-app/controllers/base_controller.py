from abc import ABC, abstractmethod

from models import Model

class Controller(ABC):
    
    @abstractmethod
    def run(self):
        pass

    
    @abstractmethod
    def update_display(self):
        pass

    
    @property
    @abstractmethod
    def model(self) -> Model:
        pass
    
    
    @model.setter
    @abstractmethod
    def model(self, value: Model):
        pass