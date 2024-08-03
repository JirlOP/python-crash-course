
class Student:
    """
    Student info class
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)


student1 = Student("John", 25)
student2 = Student("John", 25)

# they are different instances
print(student1)
print(student2)

student2 = student1
# they are the same instance
print(student1)
print(student2)

