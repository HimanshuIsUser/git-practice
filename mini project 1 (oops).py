# list = ["Rich dad","Harry Potter","Batman","Think And Grow Rich","Genghis Khan"]
# dict_nry = {("books"):("himanshu"),("bansal"):("manish")}
# print("\t\tWELCOME TO LIBRARY")
# print("\nHow Can I Help You :-")
# print("A  Dsplay The Books\nB = Lend The Book\nC = Donate Any Book\nD = Details Of Any Leanded Books")
# while True:
#     first_input = input("\nChose One Of Given :-")
#     if(first_input == "A"):
#         print("\nBOOKS :-\n")
#         for item in list:
#             print(item)
#     elif(first_input == "B"):
#         with open("library_func.text","a") as libry:
#             libry.write(str(input("\nEnter your name :-") + "\t:-\t"))
#             libry.write(str(input("Enter book name :-")+"\n"))
#         print("Thank you so much")
#     elif(first_input == "C"):
#         list.append(str(input("Enter the name of book :-")))
#         print("Thank you")
#     elif(first_input == "D"):
#         with open("library_func.text","r") as libry:
#             print(libry.read())
#             print("Thank you sir")
#     elif(first_input == "E"):
#         print(dict_nry[input()])
#     elif(first_input =="F"):
#         print(dict_nry.update({input():input()}))
#........................................................................................................
#class type mini project
class library_1:
    def __init__(self,name,list):
        self.name = name
        self.list = list
        self.dictn_ry = {}
    def lend_books(self):
        lend_name = input("Enter your name")
        lend_book = input("enter The book name")
        if(lend_book not in self.dictn_ry.keys()):
            self.dictn_ry.update({lend_book:lend_name})
        else:
            print("sorry the book is already in use :-",student.dictn_ry)
    def return_book(self):
        book=input("Enter the name of book")
        name = input("Enter your name")
        self.dictn_ry.pop(book,name)
    def add_book(self):
        self.list.append(input("Enter the name of book"))
student = library_1("harry",["Rich Dad","Pyshocology Of Money","Mahabharat","Jacksparrow","Ramayan"])
while True:
    print("what would you like to do")
    print("a = display the book of library\nb = Return book\nc = lend book\nd = To view the history of books\ne = To donate any book")
    fun_T = input()
    if fun_T == "a":
        print(student.list)
    elif(fun_T == "b"):
        student.return_book()
    elif(fun_T == "c"):
        student.lend_books()
    elif(fun_T == "d"):
        print(student.dictn_ry)
    elif(fun_T=="e"):
        student.add_book()
    else:
        print("invalid input")
    print("to Quit enter Q :-\nTo Continue Enter C:-")
    loop_c=""
    while(loop_c!="q" and loop_c!="c"):
        loop_c = input()
        if(loop_c== "q"):
            print("HAVE A NICE DAY")
            exit()
        elif(loop_c=="c"):
            continue


