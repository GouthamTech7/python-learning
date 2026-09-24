Student_name = input("Enter your name: ")
maths = int(input("Enter your Maths marks: "))
physics = int(input("Enter your Physics marks: "))
english = int(input("Enter your English marks: "))

total_marks = maths + physics + english
average_marks = total_marks / 3

print("Student Name:", Student_name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

if average_marks >= 90:
    print("Grade: A")   

elif average_marks >= 80:
    print("Grade: B")

elif average_marks >= 70:
    print("Grade: C")   

elif average_marks >= 60:
    print("Grade: D")   

else:
    print("Grade: F")

    