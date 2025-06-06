"""
Requirements:

1.	Define an abstract base class or interface PaymentMethod with:
    o	An abstract method process_payment(amount: float)
    o	An abstract method validate() (can be overridden for specific validation logic).

2.	Create at least three concrete subclasses:
    o	CreditCardPayment: Validates card number and processes payment.
    o	PayPalPayment: Validates email and simulates login before processing.
    o	CryptoPayment: Simulates checking a wallet and confirms blockchain transfer.

3.	Create a function checkout(payment: PaymentMethod, amount: float) that:
    o	Calls validate() on the payment method.
    o	Calls process_payment(amount) to complete the transaction.

4.	In the main/test function:
    o	Instantiate each payment type with sample data.
    o	Call checkout() using different payment objects.
    o	Demonstrate that different payment behaviors are triggered using polymorphism.

Expected Concepts Demonstrated:
•	Abstract classes/interfaces
•	Method overriding
•	Polymorphic function calls
•	Use of a single interface for varied behaviors
"""



from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

    @abstractmethod
    def validate(self):
        pass


class CreditCardPayment(PaymentMethod):
    """Validates card number and processes payment."""

    def __init__(self, user_card_number):
        self.user_card_number = user_card_number
        self.registered_card_numbers = [
            "1111111111111111",
            "2222222222222222",
            "3333333333333333",
            "4444444444444444",
            "5555555555555555"
        ]

    def validate(self) -> bool:
        print(f"Validating credit card number: {self.user_card_number}")

        try:
            for i in self.user_card_number:
                int(i)
        except ValueError:
            print("\tInvalid credit card number")
            print("\tThere shouldn't be any non-digit character")
            return False
        
        if len(self.user_card_number) != 16:
            print("\tInvalid credit card number")
            print("\tIt must be exactly 16 digits")
            return False
        
        if self.user_card_number not in self.registered_card_numbers:
            print("\tNo match found")
            return False

        print("\tDone")
        return True

    def process_payment(self, amount: float):
        print(f"Processing credit card payment...")
        print("\tDone")
        print(f"Payment successful: ₱{round(amount, 2):,}")


class PayPalPayment(PaymentMethod):
    """Validates email and simulates login before processing."""

    def __init__(self, user_email):
        self.user_email = user_email
        self.registered_emails = [
            "juan.delacruz@example.com",
            "maria.clara@gmail.com",
            "andres.bonifacio@yahoo.com",
            "gabriela.silang@domain.ph",
            "apolinario.mabini@sub.domain.net"
        ]

    def validate(self) -> bool:
        print(f"Validating email address: {self.user_email}")
        
        if ("@" not in self.user_email) or ("." not in self.user_email.split("@")[1]):
            print("\tInvalid email address")
            print("\tUnrecognized email format")
            return False
        
        if self.user_email not in self.registered_emails:
            print("\tNo match found")
            return False
        
        print("\tDone")
        return True

    def process_payment(self, amount: float):
        print(f"Processing PayPal payment...")
        print("\tDone")
        print(f"Payment successful: ₱{round(amount, 2):,}")


class CryptoPayment(PaymentMethod):
    """Simulates checking a wallet and confirms blockchain transfer."""

    def __init__(self, user_wallet_id):
        self.user_wallet_id = user_wallet_id
        self.wallet_ids = [
            "id_11111",
            "id_22222",
            "id_33333",
            "id_44444",
            "id_55555",
        ]
    
    def validate(self) -> bool:
        print(f"Validating wallet ID: {self.user_wallet_id}")
        
        if len(self.user_wallet_id) != 8:
            print("\tInvalid wallet ID")
            print("\tIt must be exactly 8 digits")
            return False
        
        if "id_" not in self.user_wallet_id:
            print("\tInvalid wallet ID")
            print("\tUnrecognized ID format")
            return False
        
        if self.user_wallet_id not in self.wallet_ids:
            print("\tNo match found")
            return False
        
        print("\tDone")
        return True

    def process_payment(self, amount: float):
        print(f"Processing Crypto payment...")
        print("\tDone")
        print(f"Blockchain transfer successful: ₱{round(amount, 2):,}")


def checkout(payment: PaymentMethod, amount: float):
    is_valid = payment.validate()
    if is_valid:
        payment.process_payment(amount)

def main():
    credit = CreditCardPayment("1111111111111111")
    paypal = PayPalPayment("juan.delacruz@example.com")
    crypto = CryptoPayment("id_33333")

    i = 80
    print("="*i) 
    print("Credit Card".center(i))
    print("="*i) 
    checkout(payment=credit, amount=1400.88)    
    print("="*i) 
    print("PayPal".center(i))
    print("="*i) 
    checkout(payment=paypal, amount=5000.58888)    
    print("="*i) 
    print("Crypto".center(i))
    print("="*i) 
    checkout(payment=crypto, amount=23434.123488)    
    

if __name__ == "__main__":
    main()