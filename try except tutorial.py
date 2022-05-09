#tyr except method :-
# print("enter your num1 \n")
# num1=input()
# print("enter your num2 \n")
# num2=input()
# try:
#     print("the sum of two number is = ",int(num1) + int(num2))
# except Exception as him:
#     print(him)
# print("you work has done")
#..................................................................
#try except finally method with else also:-
# loop_1 = ["manish","bansal","gourav"]
# for item in loop_1:
#     if item =="gourav":
#         try:
#             print("hello")
#         except Exception as e:
#             print(e)
#         else:
#             print("mahima")
#         finally:
#             print("sorry")
#     else:
#         print("false")
#....................................................................
# raise methods :-
while True:
    a=input("enter your name :- ")
    try:
        print(c)
    except Exception as e:
        if a=="manish":
            raise ValueError("you are not allowed for this function!")
