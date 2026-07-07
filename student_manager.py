student = []


#creating menu 
def menu():
    print("=" *30)
    print("Student Management System")
    print("=" *30)
    print("1. Show Student")
    print("2. Add Student")
    print("3. Remove Student")
    print("4. Total Students")
    print("5. Exit")
    
menu()

def show_students():
    print("=" * 30)
    print("List of Students:", student)
    
    
def add_student():
    name =input("enter student name:")
    student.append(name)
    print("Student added successfully.")
    print(student)
    
def remove_student():
    name = input ("enter student name to remove:")
    student.remove(name)
    print("Student removed successfully.")
    print(student)
    
def total_students():
     print("Total no of students:", len(student))
     
def exit_program():
    print("Exiting the program. Goodbye!")
    

    

choice = input("Choose an option:")
if choice =="1":
    show_students()
elif choice =="2":
    add_student()
    
elif choice =="3":
    remove_student()
elif choice =="4":
   total_students()
elif choice =="5":
      exit_program()
else:
    print("Invalid choice. Please try again.")
