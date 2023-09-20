import math
import random

class AccountService:
    
    def generate_account_number(self) -> int:
        return math.floor(random.random() * 1000000)
    
class Account:
    def __init__(self, account_number: int, customer_name: str, customer_address: str, balance: float):
        self.account_number = account_number
        self.balance = balance
        self.customer_name = customer_name
        self.customer_address = customer_address

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Amount must be not negative")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Amount must be more than you have on balance")
        self.balance -= amount

    def str(self):
        return f"Account {self.account_number} by {self.customer_name} ({self.customer_address}), balance {self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, customer_name: str, customer_address: str, initial_balance: float) -> Account:
        account_number = AccountService().generate_account_number()
        account = Account(account_number, customer_name, customer_address, initial_balance)
        if account_number in self.accounts:
            raise ValueError("Key already exist")
        else:
            self.accounts[account_number] = account
            return account     

    def get_account(self, account_number: int) -> Account:
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            raise ValueError("Account not found")
    
   
  
def banking_scenario():
    bank = Bank()
    
    alice_account = bank.create_account("Alice", "Sankt Peterburg", 1000)
    bob_account = bank.create_account("Bob", "Moscow", 300)

    alice_account.deposit(200.00)
    print(f"Alice's balance: {alice_account.balance}")
    bob_account.deposit(700)
    print(f"Bob's balance: {bob_account.balance}")
    alice_account.withdraw(150)
    print(f"Alice's balance: {alice_account.balance}")
    # Alice opens an account and deposits some money)
    try:
        alice_account.withdraw(1500.0)
    except ValueError as e:
        print(e)  # Insufficient funds
    # Bank retrieves Alice's account using the account number
    retrieved_account = bank.get_account(alice_account.account_number)
    print(f"Account {retrieved_account.account_number} by {retrieved_account.customer_name} ({retrieved_account.customer_address}), balance {retrieved_account.balance}") # Account XXXXXX by Alice (Moscow, Stremyannyi per, 1), balance 300.0
    
if __name__ == "__main__":
    banking_scenario()    