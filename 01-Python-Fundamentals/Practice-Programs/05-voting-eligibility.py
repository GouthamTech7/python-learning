Name = input("Enter your name: ")
age = int(input("Enter your age: "))
citizenship = input("Are you an Indian citizen? (yes/no): ")

if age >= 18 and citizenship == "yes":
    print(Name + ", you are eligible to vote.")
else:
    print(Name + ", you are not eligible to vote.")