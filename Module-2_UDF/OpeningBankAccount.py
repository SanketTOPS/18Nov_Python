# Header: Opening bank account 

balance = 0.0

def create_account():
    global balance  # Use the global balance variable
    account_number = input("Enter account number: ")
    account_holder_name = input("Enter account holder name: ")
    account_type = input("Enter account type (Savings/Current): ")
    balance = 0.0  # Initialize the global balance
    return {
        "account_number": account_number,
        "account_holder_name": account_holder_name,
        "account_type": account_type,
    }

def deposit(account):
    global balance  # Use the global balance variable
    amount = float(input("Enter amount to deposit (minimum $2000): "))
    if amount >= 2000:
        balance += amount
        print(f"Deposited: ${amount:.2f}. New balance: ${balance:.2f}")
    else:
        print("Error: Minimum deposit amount is $2000.")

def withdraw(account):
    global balance  # Use the global balance variable
    amount = float(input("Enter amount to withdraw: "))
    if 0 < amount <= balance:
        balance -= amount
        print(f"Withdrew: ${amount:.2f}. New balance: ${balance:.2f}")
    else:
        print("Error: Insufficient funds or invalid amount.")

def print_account_statement(account):
    print("\n--- Account Statement ---")
    print(f"Account Number: {account['account_number']}")
    print(f"Account Holder Name: {account['account_holder_name']}")
    print(f"Account Type: {account['account_type']}")
    print(f"Total Balance: ${balance:.2f}")  # Use the global balance variable

def main():
    account = create_account()

    while True:
        print("\n--- Bank Management System ---")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Print Account Statement")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            deposit(account)
        elif choice == '2':
            withdraw(account)
        elif choice == '3':
            print_account_statement(account)
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()