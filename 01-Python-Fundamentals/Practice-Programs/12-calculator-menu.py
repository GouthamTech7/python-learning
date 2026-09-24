num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction") 
print("3. Multiplication")
print("4. Division")

operation = input("Enter the number corresponding to the operation you want to perform (1/2/3/4): ")

if operation =="1":
    result = num_1 + num_2
    print("Result:", result)
elif operation == "2":
    result = num_1 - num_2
    print("Result:", result)
elif operation == "3":
    result = num_1 * num_2
    print("Result:", result)
elif operation == "4":
    result = num_1 / num_2
    print("Result:", result)
else:
    print("Invalid operation selected.")
    