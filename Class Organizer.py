classmates = ["Arav" , "Priya" , "Rahul" , "Sneha" , "Dev"]

print("Class list" , classmates)

print("Total Students",len(classmates))

print("Total Students",classmates[0])

print("Total Students",classmates[-1])

print("Total Students",classmates[3])

classmates.append("Meera")

print("\n After adding Meera",classmates)

classmates.remove("Dev")

print("\n After removing Dev",classmates)

classmates.sort()

print("\n Sorted Alphabiticallly",classmates)

classmates.reverse()

print("\n sorted reversed",classmates)

teacher = {"name" : "Mr Sharma" ,  "Subject" : "Python" , "experience" : 5}

print("\n Teacher Profile" , teacher)

print("Subject:" , teacher["Subject"])

print("Experience:" , teacher.get("experience" , "Not found"))

teacher["experience"] = 6

teacher["email"] = "sharma@school.com"

teacher.pop("experience")

print("Updated teacher profile:" , teacher)




roll_numbers = [1,2,3,4,5]

names = ["Arav" , "Priya" , "Rahul" , "Sneha" , "Dev"]

student_directory = dict(zip(roll_numbers , names))

print(" \n  Student Directory:" , student_directory)

print("Student at Roll 3:" , student_directory[3])

















