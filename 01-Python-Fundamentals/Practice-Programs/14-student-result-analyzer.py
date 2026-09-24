name = input("Enter your name: ")
maths_marks = int(input("Enter your Maths marks: "))
physics_marks = int(input("Enter your Physics marks: "))
chemistry_marks = int(input("Enter your Chemistry marks: "))    

total_marks = maths_marks + physics_marks + chemistry_marks
average_marks = total_marks / 3
print("Student Name:", name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

if maths_marks >= 40 and physics_marks >= 40 and chemistry_marks >= 40: 
    print("Result: Pass")

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

else:
    print("Result: Fail")
    


