

balance = 5000


print("Welcome to the ATM Simulator!")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    print("Your current balance:", balance)
elif choice == "2":
    deposit = int(input("Enter the amount to deposit: "))
    balance = deposit + balance
    print("New Balance:", balance)
elif choice == "3":
    withdraw = int(input("Enter the amount to withdraw: "))
    if withdraw > balance:
        print("Insufficient funds")
    else:
        balance = balance - withdraw
        print("New Balance:", balance)
else:
    print("Invalid Choice")
    
