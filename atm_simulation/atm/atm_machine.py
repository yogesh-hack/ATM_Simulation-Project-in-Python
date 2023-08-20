import time
import sys
import shutil
from .bank_account import BankAccount


class ATM:
    def __init__(self, bank_accounts):
        self.bank_accounts = bank_accounts

    def display_menu(self):
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")


    def print_centered(self, text):
        terminal_width = shutil.get_terminal_size().columns
        padding = (terminal_width - len(text)) // 2
        print(" " * padding + text)

    def print_with_typewriter_effect(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)  # Adjust the delay to control the typing speed
        print()

    def loading_effect(self, text, delay=0.1):
        for _ in range(3):
            sys.stdout.write("\r" + text + "   ")
            sys.stdout.flush()
            time.sleep(delay)
            sys.stdout.write("\r" + " " * len(text) + "   ")
            sys.stdout.flush()
            time.sleep(delay)

    def run(self):
        while True:
            self.loading_effect("Loading ATM...")
            self.print_centered("""
 _      __    __                   __       ___ ________  ___
| | /| / /__ / /______  __ _  ___ / /____  / _ /_  __/  |/  /
| |/ |/ / -_) / __/ _ \/  ' \/ -_) __/ _ \/ __ |/ / / /|_/ / 
|__/|__/\__/_/\__/\___/_/_/_/\__/\__/\___/_/ |_/_/ /_/  /_/  
            """)
            account_number = input("Enter your account number: ")

            if account_number in self.bank_accounts:
                account = self.bank_accounts[account_number]
                account_name = account.get_account_name()  # Get the account name
                self.print_with_typewriter_effect(f"Hello, {account_name}!")
                self.display_menu()

                choice = input("Enter your choice: ")

                if choice == '1':
                    print(f"Balance: ${account.check_balance()}")

                elif choice == '2':
                    amount = float(input("Enter amount to deposit: $"))
                    if account.deposit(amount):
                        print("Deposit successful.")
                    else:
                        print("Invalid amount.")

                elif choice == '3':
                    amount = float(input("Enter amount to withdraw: $"))
                    if account.withdraw(amount):
                        print("Withdrawal successful.")
                    else:
                        print("Insufficient funds or invalid amount.")

                elif choice == '4':
                    self.print_with_typewriter_effect("Thank you for using the ATM!")
                    break

                else:
                    print("Invalid choice. Please select again.")

            else:
                print("Account not found. Please try again.")
