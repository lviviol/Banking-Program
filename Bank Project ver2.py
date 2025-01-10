#Create Python Banking Program
#Credits Bro Code https://www.youtube.com/watch?v=JlMyYuY1aXU
#Credit https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/

#Enhancement made to reject non FLOAT input with try-except block
#Enhance made to simulate "Lock" after 3 invalid inputs 
#Enhance made to add countdown timer for "Lock"

import time

def show_balance(balance):
    print(f"\nYour balance is ${balance:.2f}")

def deposit(attempts=3):
    if attempts == 0:
        print("\nToo many invalid attempts.  Your account is locked for security reasons.  Please try again later.")
        print ("\nTime left ")
        countdown(10)
        return 0

    try:
        amount = float(input("\nEnter deposit amount $"))
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
        print ("\nTime left ")
        countdown(10)
        return 0

    try:
        amount = float(input("\nEnter withdrawal amount $"))
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


#countdown(t)
def countdown(t):
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1


def main():
    balance = 0
    is_running = True

    while is_running:
        print("\n\nWelcome to your Friendly Bank")
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

    print("\nThank you for banking with us.\n")


if __name__ == '__main__': #Makes sure the program runs when the file is executed
    main()









#Timer Code *****************
#Credit https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
#import time

#def countdown(t): 
    
#    while t: 
#        mins, secs = divmod(t, 60) 
#        timer = '{:02d}:{:02d}'.format(mins, secs) 
#        print(timer, end="\r") 
#        time.sleep(1) 
#        t -= 1
      
#    print('Fire in the hole!!') 
  
# input time in seconds 
#t = input("Enter the time in seconds: ") 
#t = 10 
  
# function call 
#countdown(int(t)) 



