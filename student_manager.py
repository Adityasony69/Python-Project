student = []


#creating menu 
def menu():
    print("=" *30)
    print("Student Management System")
    print("=" *30)
    print("1. Show Student")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Remove Student")
    print("5. Total Students")
    print("6. Exit")
    

def show_students():
    print("=" * 30)
    print("List of Students:", student)
    
    
def add_student():
    name =input("enter student name:")
    student.append(name)
    print("Student added successfully.")
    print(student)
    
def search_student():
    name = input("enter student name to  search:")
    if name in student:
        print("student is found in the list.")
    else:
        print(name + " student is not found in the list.")
    
def remove_student():
    name = input ("enter student name to remove:")
    student.remove(name)
    print("Student removed successfully.")
    print(student)
    
def total_students():
     print("Total no of students:", len(student))
     
def exit_program():
    print("Exiting the program. Goodbye!")
    

running = True
while running:
    menu()
    choice = input("Choose an option:")
    if choice =="1":
        show_students()
    elif choice =="2":
        search_student()
    elif choice =="3":
        add_student()
    elif choice =="4":
        remove_student()
    elif choice =="5":
        total_students()
    elif choice =="6":
      exit_program()
      exit()
    else:
        print("Invalid choice. Please try again.")

    

