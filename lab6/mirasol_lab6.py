class BankAccount:
    def __init__(self, owner, password, balance=0, overdraft_limit=0, interest_rate=0.01):
        self.__owner = owner
        self.__password = password
        self.__balance = balance
        self.__overdraft_limit = overdraft_limit
        self.__interest_rate = interest_rate
        self.__transaction_history = []

    # getters

    def get_owner(self):
        return self.__owner
    
    def get_password(self):
        return self.__password

    def get_balance_1(self):
        return self.__balance

    def get_overdraft_limit(self):
        return self.__overdraft_limit

    def get_interest_rate(self):
        return self.__interest_rate

    def get_transaction_history(self):
        return self.__transaction_history
    
    # setters
    
    def set_owner(self, owner):
        self.__owner = owner

    def set_password(self, password):
        self.__password = password

    def set_balance(self, balance):
        self.__balance = balance

    def set_overdraft_limit(self, limit):
        self.__overdraft_limit = limit

    def set_interest_rate(self, rate):
        self.__interest_rate = rate

    def set_transaction_history(self, transaction):
        self.__transaction_history.append(transaction)

    # functionalities

    def authenticate(self, password):
        return self.get_password() == password

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited Php{amount}")
            print(f"{self.owner}: Deposited Php{amount}. New balance is Php{self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew Php{amount}")
            print(f"{self.owner}: Withdrew Php{amount}. New balance is Php{self.balance}.")
        else:
            print("Withdrawal exceeds overdraft limit.")

    def get_balance(self):
        print(f"{self.owner}: Current balance is Php{self.balance}.")
        return self.balance

    def apply_interest(self):
        if self.balance > 0:
            interest = self.balance * self.interest_rate
            self.balance += interest
            self.transaction_history.append(f"Interest applied: Php{interest:.2f}")
            print(f"{self.owner}: Interest of Php{interest:.2f} applied. New balance is Php{self.balance:.2f}.")
        else:
            print("No interest applied on negative or zero balance.")

    def show_transaction_history(self):
        print(f"{self.owner}: Transaction History:")
        for transaction in self.transaction_history:
            print(f"- {transaction}")

    # property classes

    owner = property(get_owner, set_owner)
    password = property(get_password, set_password)
    balance = property(get_balance_1, set_balance)
    overdraft_limit = property(get_overdraft_limit, set_overdraft_limit)
    interest_rate = property(get_interest_rate, set_interest_rate)
    transaction_history = property(get_transaction_history, set_transaction_history)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner, password, balance=0, overdraft_limit=0, interest_rate=0.01):
        if owner in self.accounts:
            print("Account already exists for this owner.")
            return
        self.accounts[owner] = BankAccount(owner, password, balance, overdraft_limit, interest_rate)
        print(f"Account created for {owner}.")

    def login(self, owner, password):
        account = self.accounts.get(owner)
        if account and account.authenticate(password):
            print(f"Login successful for {owner}.")
            return account
        else:
            print("Invalid credentials.")
            return None

def main():
    bank = Bank()
    while True:
        print("\n=== Welcome to the Bank System ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            owner = input("Enter username: ")
            password = input("Enter password: ")
            balance = float(input("Initial balance: "))
            overdraft = float(input("Overdraft limit: "))
            interest = float(input("Interest rate (e.g. 0.05 for 5%): "))
            bank.create_account(owner, password, balance, overdraft, interest)

        elif choice == "2":
            owner = input("Enter username: ")
            password = input("Enter password: ")
            account = bank.login(owner, password)
            if account:
                while True:
                    print(f"\n--- {owner}'s Menu ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Apply Interest")
                    print("5. View Transaction History")
                    print("6. Logout")
                    action = input("Select action: ")

                    if action == "1":
                        amount = float(input("Amount to deposit: "))
                        account.deposit(amount)
                    elif action == "2":
                        amount = float(input("Amount to withdraw: "))
                        account.withdraw(amount)
                    elif action == "3":
                        account.get_balance()
                    elif action == "4":
                        account.apply_interest()
                    elif action == "5":
                        account.show_transaction_history()
                    elif action == "6":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option.")
        elif choice == "3":
            print("Exiting the bank system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()