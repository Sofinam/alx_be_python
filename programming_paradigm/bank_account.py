import sys

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        
        initailise a new BankAccount instance.
        :param initial_balance: Initial balance for the account, defaults to 0.
        """
        self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        :param amount: The amount to deposit.
        """
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        """
        withdraw a specified amount from the account if sufficient funds are available.
        :param amount: The amount to withdraw.
        :return: True if withdrawal is successful, False otherwise.
        """

        if 0 < amount <= self.__account_balance:
            self._account_balance -= amount
            return True
        return False
    def display_balance(self):
        """
        Display the current account balance.
        """

        print(f"Current Balance: ${self._account_balance:.2f}")
        
def main():
        account = BankAccount(100)
        if len(sys.argv) < 2:
            print("Usage: python main.py <command>:<amount>")
            print("Commands: deposit, withdraw, display")
            sys.exit(1)

        command, *params = sys.argv[1].split(':')
        amount = float(params[0]) if params else None

        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount}")
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"withdrew: ${amount}")
            else:
                print("Insufficient funds.")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command.")
if __name__ == "__main__":
   main()        
        
        
