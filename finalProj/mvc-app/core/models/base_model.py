from abc import ABC, abstractmethod
from typing import List, Dict, Tuple
from backend import Transaction, TransactionManager, UserRepository


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
    def load_transactions_per_filter(self) -> Dict[str, List[Transaction]]:
        pass


    @abstractmethod
    def load_amounts(self):
        pass