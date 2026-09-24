username = input("Enter your username: ")
password = input("Enter your password: ")

if username != "admin":
    print("Invalid username")

elif password != "Cyber@123":
    print("Incorrect password")

else:
    print("Login successful!")
    