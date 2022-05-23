#1 Define a Python class Student(). Using  attributes and methods display the info about student.
# class Studient:
#     def __init__(self,clas,birthday, school, Name):
#         self.clas = clas
#         self.birthday = birthday
#         self.school =school
#         self.Name = Name
#     def Display(self):
#         print(f"Studient name {self.Name} birthday is {self.birthday} studient school is {self.school} and studient in {self.clas} class")
# p1 = Studient("5", "01.09.2005", "160", "Anri")
# p1.Display()

#2Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
#Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
#Create a method display() that display the length, width,
#perimeter and area of an object created using an instantiation on rectangle class.

# class Rectangle:
#     def __init__(self, length , width):
#         self.length = length
#         self.width = width
#     def Perimeter(self):
#         return 2*(self.length + self.width)
#     def Area(self):
#         return self.length*self.width   
#     def display(self):
#         print("The length of rectangle is: ", self.length)
#         print("The width of rectangle is: ", self.width)
#         print("The perimeter of rectangle is: ", self.Perimeter())
#         print("The area of rectangle is: ", self.Area())
# class Parallelepipede(Rectangle):
#     def __init__(self, length, width , height):
#         Rectangle.__init__(self, length, width)
#         self.height = height
#     def volume(self):
#         return self.length*self.width*self.height      
# myRectangle = Rectangle(7 , 5)
# myRectangle.display()
# print("----------------------------------")
# myParallelepipede = Parallelepipede(7 , 5 , 2)
# print("the volume of myParallelepipede is: " , myParallelepipede.volume())

#3Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor:
#Define a Area() method of the class which calculates the area of ​​the circle.
#Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

# from math import pi
# class Circle:
#     def __init__(self, a, b, r):
#         self.a = a
#         self.b = b
#         self.r = r
#     def perimeter (self):
#         return  2 * pi * self.r
#     def area (self):
#         return  pi * self.r**2
# C = Circle(4,3,5)
# print ("the perimeter of the circle C is:", C.perimeter() )
# print ("the area of circle C is:", C.area())

# #4 Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method  which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details.

class BankAccount: 
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def Deposit(self , d ):
        self.balance = self.balance + d
        print("Success")
    def Withdrawal(self , w):
        if(self.balance < w):
            print("Insufficient balance !")
        else:
            self.balance = self.balance - w
            print("Success")
    def bankFees(self):
        self.balance = (95/100)*self.balance
        print("Success")
    def display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance , " $")
Account = BankAccount(777, "Anri Hayrapetyan" , 100)
Account.Withdrawal(100)
Account.Deposit(2000)
Account.display()