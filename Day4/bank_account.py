class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance
        self._transaction_history = []
        self._validate_initial_balance()
        self._log_transaction("Account Created", balance)

    def _validate_initial_balance(self):
        """Validates initial balance"""
        if self._balance < 0:
            raise ValueError("Initial balance cannot be negative")
        if not isinstance(self._balance, (int, float)):
            raise TypeError("Balance must be a number")

    def _log_transaction(self, transaction_type, amount):
        """Logs all transactions"""
        self._transaction_history.append({
            'type': transaction_type,
            'amount': amount,
            'balance_after': self._balance
        })

    def deposit(self, amount):
        """Deposits money into the account"""
        # Validation
        if not isinstance(amount, (int, float)):
            return {
                'success': False,
                'message': "Deposit amount must be a number",
                'current_balance': self._balance
            }

        if amount <= 0:
            return {
                'success': False,
                'message': "Deposit amount must be greater than 0",
                'current_balance': self._balance
            }

        # Process deposit
        self._balance += amount
        self._log_transaction("Deposit", amount)

        return {
            'success': True,
            'message': f"Successfully deposited ${amount:.2f}",
            'amount_deposited': amount,
            'current_balance': self._balance
        }

    def withdraw(self, amount):
        """Withdraws money from the account"""
        # Validation
        if not isinstance(amount, (int, float)):
            return {
                'success': False,
                'message': "Withdrawal amount must be a number",
                'current_balance': self._balance
            }

        if amount <= 0:
            return {
                'success': False,
                'message': "Withdrawal amount must be greater than 0",
                'current_balance': self._balance
            }

        if amount > self._balance:
            return {
                'success': False,
                'message': f"Insufficient funds! You tried to withdraw ${amount:.2f}, but only have ${self._balance:.2f}",
                'current_balance': self._balance,
                'shortage': amount - self._balance
            }

        # Process withdrawal
        self._balance -= amount
        self._log_transaction("Withdrawal", amount)

        return {
            'success': True,
            'message': f"Successfully withdrew ${amount:.2f}",
            'amount_withdrawn': amount,
            'current_balance': self._balance
        }

    def get_balance(self):
        """Returns current balance"""
        return {
            'owner': self._owner,
            'balance': self._balance,
            'formatted_balance': f"${self._balance:.2f}"
        }

    def display_balance(self):
        """Displays current balance in a formatted way"""
        result = self.get_balance()
        print(f"\n{'=' * 40}")
        print(f"Account Owner: {result['owner']}")
        print(f"Current Balance: {result['formatted_balance']}")
        print(f"{'=' * 40}\n")

    def display_transaction_history(self):
        """Displays all transactions"""
        print(f"\n{'=' * 50}")
        print(f"TRANSACTION HISTORY - {self._owner}")
        print(f"{'=' * 50}")

        if not self._transaction_history:
            print("No transactions found")
        else:
            for idx, transaction in enumerate(self._transaction_history, 1):
                print(
                    f"{idx}. {transaction['type']:<15} | Amount: ${transaction['amount']:<10.2f} | Balance: ${transaction['balance_after']:.2f}")

        print(f"{'=' * 50}\n")

    def transfer(self, other_account, amount):
        """Transfers money to another account"""
        if not isinstance(other_account, BankAccount):
            return {
                'success': False,
                'message': "Invalid recipient account"
            }

        # Withdraw from current account
        withdrawal_result = self.withdraw(amount)

        if not withdrawal_result['success']:
            return withdrawal_result

        # Deposit to recipient account
        deposit_result = other_account.deposit(amount)

        if not deposit_result['success']:
            # Rollback if deposit fails
            self._balance += amount
            return {
                'success': False,
                'message': f"Transfer failed during deposit: {deposit_result['message']}"
            }

        return {
            'success': True,
            'message': f"Successfully transferred ${amount:.2f} to {other_account._owner}",
            'amount_transferred': amount,
            'your_new_balance': self._balance,
            'recipient_new_balance': other_account._balance
        }

    def __str__(self):
        """String representation"""
        return f"{self._owner}'s Account - Balance: ${self._balance:.2f}"

    def __repr__(self):
        """Object representation"""
        return f"BankAccount(owner='{self._owner}', balance={self._balance})"


# Usage Examples
print("=" * 50)
print("BANK ACCOUNT SYSTEM DEMO")
print("=" * 50)

# Create accounts
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

# Display initial balance
account1.display_balance()

# Deposit money
print("1. DEPOSIT OPERATION")
result = account1.deposit(500)
print(f"Status: {result['message']}")
print(f"New Balance: {result['current_balance']}\n")

# Successful withdrawal
print("2. WITHDRAWAL OPERATION (Success)")
result = account1.withdraw(200)
print(f"Status: {result['message']}")
print(f"New Balance: {result['current_balance']}\n")

# Failed withdrawal (insufficient funds)
print("3. WITHDRAWAL OPERATION (Failed - Insufficient Funds)")
result = account1.withdraw(2000)
print(f"Status: {result['message']}")
print(f"Current Balance: {result['current_balance']}\n")

# Invalid deposit
print("4. INVALID DEPOSIT (Negative Amount)")
result = account1.deposit(-100)
print(f"Status: {result['message']}\n")

# Display transaction history
account1.display_transaction_history()

# Transfer between accounts
print("5. TRANSFER OPERATION")
result = account1.transfer(account2, 300)
print(f"Status: {result['message']}")
print(f"Alice's New Balance: ${result['your_new_balance']:.2f}")
print(f"Bob's New Balance: ${result['recipient_new_balance']:.2f}\n")

# Display final balances
print("FINAL ACCOUNT DETAILS")
account1.display_balance()
account2.display_balance()

# Display both transaction histories
account1.display_transaction_history()
account2.display_transaction_history()