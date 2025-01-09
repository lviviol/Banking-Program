#Create Python Banking Program
#Credits Bro Code https://www.youtube.com/watch?v=JlMyYuY1aXU
#Enhancement made to reject non FLOAT input with try-except block
#Enhance made to simulate "Lock" after 3 invalid inputs 

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit(attempts=3):
    if attempts == 0:
        print("Too many invalid attempts.  Your account is locked as for security reasons.")
        exit(1)

    try:
        amount = float(input("Enter deposit amount $"))
    except ValueError:
        print ("Only numbers are accepted.  Please try again.")
        return deposit(attempts - 1)
    
    if amount <=0:
        print("Invalid amount. Please try again.")
        return deposit(attempts - 1)
    else:
        return amount


def withdraw(balance, attempts=3):
    if attempts == 0:
        print("Too many invalid attempts.  Your account is locked as for security reasons.")
        exit(1)

    try:
        amount = float(input("Enter withdrawal amount $"))
    except ValueError:
        print ("Only numbers are accepted.  Please try again.")
        return withdraw(balance, attempts - 1)
    

    if amount > balance:
        print("Insufficient funds.  Please try again")
        return withdraw(balance, attempts - 1)
    
    elif amount <= 0:
        print("Amount must be greater than 0.  Please try again")
        return withdraw(balance, attempts - 1)
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice 1-4: ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)  
        elif choice == '4':
            is_running = False
        else:
            print("Invalid Choice. Please try again.")

    print("Thank you for banking with us.")


if __name__ == '__main__': #Makes sure the program runs when the file is executed
    main()






