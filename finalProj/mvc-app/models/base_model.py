from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def initialize_managers(self):
        pass

    @abstractmethod
    def initialize_vars(self):
        pass