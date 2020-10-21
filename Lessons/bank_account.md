# Bank Account

Using object-oriented programming concepts, your task is to create a Python program that simulates a bank account.

This bank account should all a user to do  the following:

1. Your Python program should be created in one file called `BankAccount.py`. 

1. Define a `BankAccount` class.

1. A bank account should have the following attributes:
  - `full_name` - the full name of the bank account account owner.
  - `account_number` - randomly generated 8 digit number, unique per account.
  - `routing_number` - 9 digit number, this number is the same for all accounts.
  - `balance` - the balance of money in the account, should start at 0.

4. Then define the following methods for the `BankAccount` class:
  - The `deposit` method will take one parameter `amount` and will **add** `amount` to the `balance`. Also, it will print the message: `“Amount Deposited: $X.XX”`

  - The `withdraw` method will take one parameter `amount` and will **subtract** `amount` from the `balance`. Also, it will print a message, like `“Amount Withdrawn: $X.XX”`. If the user tries to withdraw an amount that is greater than the current balance, print `”Insufficient funds.”` and charge them with an overdraft fee of `$10`.

  - The `get_balance` method will return the current `balance` of the account with a user-friendly message.

  - The `add_interest` method adds interest to the users `balance`. The annual interest rate is 1% (i.e. 0.083% per month). Thus. the balance is calculated by the following equation: `interest = balance *  0.00083 `. 

  - The `print_receipt` method prints a receipt with the account name, account number, and balance like this:
  ```
  Joi Anderson
  Account No.: ****5678
  Routing No.: 98765432
  Balance: $100.00 

  ```
  
  

