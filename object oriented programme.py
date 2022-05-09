# class student:
#     pass
# harry = student()
# larry = student()
# harry.name="himanshu"
# harry.sec="b"
# larry.name = "manish"
# larry.subjects = ["hindi","science","history"]
# print(harry.sec,larry.name,larry.subjects)
#................................................................
# class Examination:
#     no_of_leaves = 9
#     pass
# student = Examination()
# student.name = "gourav"
# student. clas = 10
# student.numbers = 500
# print(student.__dict__,"no of leaves :- ",Examination.no_of_leaves)
# print(student.clas,student.name,student.numbers)
#................................................................

# init() funtion & self() function :-
#..
#self() funtion:-

# class Numbrs:
#     def print_details(self):
#         return f"My name is {self.name} , I am a {self.role} my salary is {self.salary} "
#
# rohan=Numbrs()
# munna=Numbrs()
#
# rohan.name = "Rohan"
# rohan.role = "HR"
# rohan.salary = 80000
#
# munna.name = "munnawar"
# munna.salary = 90000
# munna.role = "enginear"
#
# print(munna.print_details())
#................................
# init() funtion  :-

# class School:
#     def __init__(self,Name,Salary,Role):
#         self.name=Name
#         self.salary = Salary
#         self.role = Role
#     @classmethod
#     def from_str(cls,string):
#         param = string.split("-")
#         return cls(param[0],param[1],param[2])
#     @staticmethod
#     def printload(string):
#         print("hello ",string)
#
# student = School("rohan",50000,"developer")
# rohan = School("munna",500000,"enginer")
# karan = School.from_str("karan-420-instructor")
# print(karan.printload("harry"))
# print(karan.__dict__)
# print(rohan.__dict__,student.__dict__)

#..................................................................
# class School:
#     leaves = 10
#     @classmethod
#     def changeleave(cls,newleaves):
#         cls.leaves=newleaves
#
# rohan=School()
# School.leaves = 10+5
# print(School.leaves)
# rohan.changeleave(0)
# print(School.leaves)
#....................................................................
# # single inheritance :-
# class programmer(School):
#     def __init__(self,name,role,salary):
#         self.name = name
#         self.role = role
#         self.salary = salary
#
#     def player(self):
#         return f"This is {self.name} .I am a {self.role} and my Salary is {self.salary}"
#
# kaju = programmer("kaju","programmer","50000")
# print(kaju.__dict__)
#.....................................................................
# multilevel class

# class electronics:
#
#     lead = 250
#     charger = 500
#     headphone = 100
#
# class phone(electronics):
#     redmi =  5000
#     nokia = 50
#
# class assecaries(phone):
#     cover = 40
#     tempered = 50
#
#
# customer = assecaries()
# print(f"customer want to buy lead and the cost is  :- {customer.lead}")
#................................................................................
# private and protective variables :- to make your code proterctive from outsiders and for make private
# class employer:
#     _leaves = 5
#     __holidays = 10
# stu = employer()
# print(stu._leaves)
# print(f"{stu._employer__holidays}")
#.................................................................................
# super() :- to handle overriding
# class A:
#     clasvar1 = "I am in the class variable A\n"
#     def __init__(self):
#         self.var1 = "i am inside class A 's constructor\n"
#         self.clasvar1 = "this is varible instance of class A\n"
#         self.special = "special\n"
# class B(A):
#     clasvar1="this is class variable B\n"
#     def __init__(self):
#         super().__init__()
#         self.clasvar1 = "this is in  the instance variable of class B\n"
#         self.var1 = "i am inside of class B 's constructor\n"
#         # print(super().clasvar1)
#
# a=A()
# b=B()
# print(b.clasvar1,b.var1,b.special)
#........................................................
# ABC abstraction :- force to use any given funtion to babies class
# from abc import ABC,abstractmethod
# class form_la(ABC):
#     @abstractmethod
#     def printform():
#         return 0
#
# class form_la1(form_la):
#     def __init__(self):
#         self.lenth = 50
#         self.breath = 20
#
# class form_la2(form_la1):
#     def printform():                    # here we have to use printform funtion because of give abstract fumtion:-
#         return f"The lenth is {lenth}"
#
# fact = form_la2()
# print(fact.lenth)
#.....................................................................
# Diamond Shape programe in multiple inheritance class :- this is a programe which creates so problems becoause of using multiple inheritance ,.so thats why many other languages dont allow to use multiple inheritance :-
# class A:
#     def printform(self):
#         print("it came from cls A")
# class B(A):
#     def printform(self):
#         print("it came from cls b")
# class C(A):
#     def printform(self):
#         print("it came from cls c")
# class D(C,B):               # Syntex of python help us to figure out the solution of diamond problem .
#     pass
# a=D()
# print(a.printform())
#.........................................................................
# DUNDER METHODS , OPERATORS AND OVERLOADING (SPECIAL METHODS) :- THESE METHODS USE FOR USEING + , / ,* , - etc:-
# class Adam:
#     # print(" my name is rohan and i am a developer , salary is 40000")
#
#     def __init__(self,aname,arole,asalary):
#         self.name = aname
#         self.role = arole
#         self.salary = asalary
#     def formate(self):
#         return f"My name is {self.name} and I am a {self.role}, my earning is {self.salary}"
#     def __repr__(self):
#         return f"A ('{self.name}','{self.role}',{self.salary})"
#     def __str__(self):
#         return f"S ('{self.name}','{self.role}',{self.salary})"
#     @classmethod
#     def print(cls):
#         print("hello")
#     def __add__(self, other):
#         return self.salary + other.salary
#     def __truediv__(self, other):
#         return self.salary / other.salary
# de=Adam("rohan","Backend developer",40000)
# ed =Adam("mohan","enginer",100000)
# print(ed+de)
# print(de)
# print(de.__dict__)
#......................................................................
# Property() and settler () :- a decorator  to make changes in run time.
#Object intro spection ;- to show cls type , and many other stuff related to details like id
class company:
    print("welcome to techworld")
    def __init__(self,fname,lname):
        self.name = fname
        self.last = lname
    def email(self):
        return f"Email :- {self.name}{self.last}@gmail.com"
    @property
    def desinger(self):
        if self.name == None or self.last == None:
            return  ("Try Again")
        return f"Email :- {self.name}{self.last}@gmail.com"
    @desinger.setter
    def desinger(self,string):
        name = string.split("@")[0]
        self.name = name.split(".")[0]
        self.last = name.split(".")[1]
    @desinger.deleter
    def desinger(self):
        self.name = None
        self.last = None

# emp1 = company(input("Enter our First Name :- "),input("Enter Your Last Name :- "))
# print(emp1.desinger())
# emp1.name = "us"
# emp1.last = "we"
# print(emp1.desinger())
#......................
emp1 = company("himanshu","bansal")
print(emp1.desinger)
emp1.desinger = "mohabbat.bintere"
print(emp1.desinger)
del emp1.desinger
print(emp1.desinger)
#.....................
print(id(emp1.last))
print(id(emp1.desinger))
print(dir(emp1))
import inspect
print(inspect.getmembers(emp1))
