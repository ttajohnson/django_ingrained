class NameOfClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        # Perform some action
        print(self.param1)


class Student:
    school = "Auburndale Intermediate School"  # Class Object Attribute

    def __init__(self, name, gpa):
        self.name = name  # Attribute
        self.gpa = gpa


stu1 = Student(name="Tim", gpa=3.5)
stu2 = Student(name="Will", gpa=2.7)

print(stu1.gpa, stu1.school)
print(stu2)


class Agent:
    origin = "USA"

    def __init__(self, codename, height, weight):
        self.codename = codename
        self.height = height
        self.weight = weight


x = Agent("Agent Redtail", 6.1, 210)
print(x.origin, x.codename, x.weight)
x.weight = 190
print(x.weight)
