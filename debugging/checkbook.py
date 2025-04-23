#!/usr/bin/python3

class Checkbook:
    """
    A simple checkbook simulator that allows users to deposit, withdraw, and check balance.

    Methods:
        deposit(amount): Adds the specified amount to the balance.
        withdraw(amount): Deducts the specified amount from the balance if sufficient funds exist.
        get_balance(): Prints the current balance.
    """

    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds the specified amount to the current balance.

        Parameters:
        amount (float): The amount to deposit.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Attempts to withdraw the specified amount from the balance.

        Parameters:
        amount (float): The amount to withdraw.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance in the checkbook.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main interactive loop that prompts the user to perform actions on the checkbook.

    Parameters:
    None

    Returns:
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

