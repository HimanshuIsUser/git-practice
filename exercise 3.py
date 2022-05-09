s=5
t=10
print("you have to enter corrcect number to win ")
print("but you have only 3 chances")
while(True):
    t=int(input())
    s=s+-1
    if(t==10) and (s<=4):
        print("you got the answer and you have left the chances = ",s)
        break
    elif (t > 10) and (s <= 4):
        print("this one is greater then the answer")
        print("and now you have left only chances = ", s)
    elif (t < 10) and (s <= 4):
        print("this one is smaller")
        print("and now you have left only chances = ", s)
    elif (s > 5):
        print("your chances are finish")
        print("try again later")
        break