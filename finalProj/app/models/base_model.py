from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def initialize_managers(self):
        pass


    @abstractmethod
    def initialize_vars(self):
        pass


    @abstractmethod
    def save_user_inputs_to_database(self):
        pass
    
    
    @abstractmethod
    def load_transactions_per_filter(self):
        pass


    @abstractmethod
    def load_amounts(self):
        pass