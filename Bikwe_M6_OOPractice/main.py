print("###This is the start of the Activity###")
print()

class Student:
    def __init__(self, name, age, major, gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I major in {self.major}.\n")

    def __str__(self):
        return f"Student(name:{self.name}, age:{self.age}, major:{self.major}, gpa:{self.gpa})\n"

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa


student1 = Student("John", 20, "Computer Science", 3.5)
student2 = Student("Jane", 22, "Mathematics", 3.8)
student3 = Student("Bob", 19, "Physics", 3.2)

print(student1)
print(student2)
print(student3)

student1.introduce()
student2.introduce()
student3.introduce()

student1.update_gpa(3.7)

print("After GPA update:")
print(student1)