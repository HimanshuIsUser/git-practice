import datetime


def getdate():
    import datetime
    return datetime.datetime.now()
print("hi")
print("Choose One Of Them :-")
print("1 = Himanshu.\n2 = Manish.\n3 = Gourav.")
name=input("Enter The Name Here :- ")
if(name=="himanshu"):
    print("what would you like to do :-")
    print("A = Log \t B = return\n")
    work1 = input()
    if (work1=="a"):
        print("Would You Like To Log In Exercise Or Diet :-")
        fit=input()
        if (fit=="diet"):
            with open("himanshu diet.text","a") as hdiet:
                data0=datetime.datetime.now()
                hdiet.write(str(data0))
                hdiet.write(input()+"\n")
        elif (fit=="exercise"):
            with open("himanshu exercise.text", "a") as hex:
                data0 = datetime.datetime.now()
                hex.write(str(data0))
                hex.write(input() + "\n")
        else:
            print("You Have Enter The Wrong Argument")
            print("Please Try Again :-")

    elif (work1=="b"):
        print("choose the following one :-")
        print("A = Diet\t\tB = Exercise\n")
        fit2=input()
        if (fit2=="diet"):
            with open("himanshu diet.text","r")as hdiet:
                content1=hdiet.read()
                print(content1)
        elif (fit2=="exercise"):
            with open("himanshu exercise.text","r")as hex:
                content2=hex.read()
                print(content2)
        else:
            print("You Have Enter The Wrong Argument")
            print("Please Try Again :-")

    else:
        print("You Have Enter The Wrong Argument")
        print("Please Try Again :-")
elif (name=="manish"):
    print("what would you like to do :-")
    print("A = Log \t B = return\n")
    work3 = input()
    if (work3 == "a"):
        print("Would You Like To Log In Exercise Or Diet :-")
        fit3 = input()
        if (fit3 == "diet"):
            with open("manish diet.text", "a") as mdiet:
                data0 = datetime.datetime.now()
                mdiet.write(str(data0))
                mdiet.write(input() + "\n")
        elif (fit3 == "exercise"):
            with open("manish exercise.text", "a") as mex:
                data0 = datetime.datetime.now()
                mex.write(str(data0))
                mex.write(input() + "\n")
        else:
            print("You Have Enter The Wrong Argument")
            print("Please Try Again :-")

    elif (work3 == "b"):
        print("choose the following one :-")
        print("A = Diet\t\tB = Exercise\n")
        fit4 = input()
        if (fit4 == "diet"):
            with open("manish diet.text", "r") as mdiet:
                content2 = mdiet.read()
                print(content2)
        elif (fit4 == "exercise"):
            with open("manish exercise.text", "r") as mex:
                content3 = mex.read()
                print(content3)
        else:
            print("You Have Enter The Wrong Argument")
            print("Please Try Again :-")

    else:
        print("You Have Enter The Wrong Argument")
        print("Please Try Again :-")
elif (name=="gourav"):
    print("what would you like to do")
    print("A = Log\t\tB = Return :-\n")
    work4 = input()
    if (work4=="a"):
        print("what would you like to select exercise or diet:-")
        bot=input("enter your selection:-\t")
        if(bot=="exercise"):
            with open("gourav exercise.text","a") as gex:
                data0=datetime.datetime.now()
                gten=gex.write(str(data0))
                gten=gex.write(input()+ "\n")
        elif (bot=="diet"):
            with open("gourav diet.text","a") as gdiet:
                data0=datetime.datetime.now()
                gten=gdiet.write(str(data0))
                gten=gdiet.write(input()+"\n")
        else:
            print("S O R R Y\nTRY AGAIN:-")
    elif(work4=="b"):
        print("what woulf you like to select exercise or diet:-")
        bot=input("enter your selection:-\t")
        if bot=="exercise":
            with open("gourav exercise.text") as gex:
                gten=gex.read()
                print(gten)
        elif bot=="diet":
            with open("gourav diet.text") as gdiet:
                gten=gdiet.read()
                print(gten)
        else:
            print("S O R R Y\t\t TRY AGAIN :-")
else:
    print("S O R R Y\t\t TRY AGAIN :-")










#     print(input("S O R R Y \t\tTry Again :-"))
# print("press A for add\npress B for get the details")
# c=input("would you like add some thing in\n your MANISH file or get to know all \ndetails that you have already in that file\n")
# if (c=="A"):
#     print("now enter your details")
#     with open("manish.txt","a") as f:
#         data0 = datetime.datetime.now()
#         f.write(str(data0))
#         f.write(input()+"\n")
#
# elif (c=="B"):
#     with open("manish.txt","r")as f:
#         content = f.read()
#         print(content)
#         print("thank you")




