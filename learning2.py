import math


class A:
    varA = "welcome to class A"


class B:
    varB = "welcome to class B"


class C(A, B):
    varC = "welcome to class C"


# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# SUPER Method  => It is used to access methods of the parent class.


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        area = math.pi * self.radius**2
        return area

    def Perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter


# c1 = Circle(10)
# print(c1.Area())
# print(c1.Perimeter())


class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Employee's Role =", self.role)
        print("Employee's Department =", self.department)
        print("Employee's Salary =", self.salary)


class Engineer(Employee):

    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age

    def showDetails(self):
        print("Engineer's Name =", self.name)
        print("Engineer's Age =", self.age)
        return super().showDetails()


# eng1 = Engineer("Ken", 20, "Full Stack Developer", "Engineering", "$120,000")
# eng1.showDetails()

class Order:
    def __init__(self, item , price):
        self.item = item
        self.price = price
    
    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = Order('Chips',10)
ord2 = Order('Biscuit',5)
print(ord1.item, ord1.price)
print(ord2.item, ord2.price)
print(ord1 < ord2)
