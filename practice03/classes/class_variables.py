# ============================================================================
# Class Variables - Class variables vs instance variables
# ============================================================================

class Student:
    """Student class showing class vs instance variables"""
    total_students = 0  # Class variable (shared by all instances)
    
    def __init__(self, name, student_id):
        self.name = name  # Instance variable
        self.student_id = student_id  # Instance variable
        Student.total_students += 1
    
    def display_info(self):
        print(f"Name: {self.name}, ID: {self.student_id}, Total students: {Student.total_students}")

student1 = Student("Alice", 101)
student1.display_info()

student2 = Student("Bob", 102)
student2.display_info()

student3 = Student("Charlie", 103)
student3.display_info()

print(f"Class variable - Total students: {Student.total_students}")
