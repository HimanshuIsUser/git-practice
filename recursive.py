# def funtion1(n):
#     if (n==1):
#         return 1
#     else:
#         return n*funtion1(n-1)
# n=int(input("enter the number"))
# print(funtion1(n))
def funtion2(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return funtion2(n-1)+funtion2(n-2)
n=int(input("enter your number"))
print("there is your answer :-",funtion2(n))