class Student:
    def __init__(self, roll_no, name, age, course):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Age: {self.age}, Course: {self.course}")


class StudentSystem:
    def __init__(self):
        self.students = []

    # Add student
    def add_student(self):
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = Student(roll_no, name, age, course)
        self.students.append(student)
        print("✅ Student Added Successfully!\n")

    # View all students
    def view_students(self):
        if not self.students:
            print("❌ No student records found!\n")
        else:
            print("\n📋 Student Records:")
            for student in self.students:
                student.display()
            print()

    # Search student
    def search_student(self):
        roll_no = input("Enter Roll No to search: ")
        found = False

        for student in self.students:
            if student.roll_no == roll_no:
                student.display()
                found = True
                break

        if not found:
            print("❌ Student not found!\n")

    # Update student
    def update_student(self):
        roll_no = input("Enter Roll No to update: ")

        for student in self.students:
            if student.roll_no == roll_no:
                student.name = input("Enter New Name: ")
                student.age = input("Enter New Age: ")
                student.course = input("Enter New Course: ")
                print("✅ Student Updated Successfully!\n")
                return

        print("❌ Student not found!\n")

    # Delete student
    def delete_student(self):
        roll_no = input("Enter Roll No to delete: ")

        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("✅ Student Deleted Successfully!\n")
                return

        print("❌ Student not found!\n")


# Main Menu
def main():
    system = StudentSystem()

    while True:
        print("====== Student Record System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            system.add_student()
        elif choice == '2':
            system.view_students()
        elif choice == '3':
            system.search_student()
        elif choice == '4':
            system.update_student()
        elif choice == '5':
            system.delete_student()
        elif choice == '6':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!\n")


if __name__ == "__main__":
    main()