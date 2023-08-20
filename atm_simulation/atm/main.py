from .bank_account import BankAccount
from .atm_machine import ATM

# Sample bank accounts
bank_accounts = {
    '123456': BankAccount('123456','Yogesh Baghel', 1000),
    '789012': BankAccount('789012','Rohan', 5000)
}


# Create and run the ATM
def main():
    atm = ATM(bank_accounts)
    atm.run()


if __name__ == "__main__":
    main()
