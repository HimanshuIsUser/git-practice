def lou_d(str):
    import win32com.client as wincl
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(str)
def funct():
    lou_d("welcome to the talketive calculator")
    while True:
        print("enter the your first value")
        lou_d("enter the your first value")
        num1=int(input())
        print("enter your second number")
        lou_d("enter the your second value")
        num2=int(input())
        print("choose one of the following one funtion")
        print("+ - %  *  / ")
        lou_d("choose one of the following one funtion")
        # lou_d(str("+ - %  *  / "))
        num3 =input()
        if num1==43 and num2==3 and num3=='*':
            print("555")
            lou_d("555")
        elif num1==56 and num2==9 and num3=='+':
            print("77")
            lou_d(str("77"))
        elif num1==56 and num2==6 and num3=='/':
            print("4")
            lou_d(str("4"))
        elif num3=='*':
            num4=num1*num2
            print(num4)
            lou_d(num4)
        elif num3=='+':
            plus=num1+num2
            print(plus)
            lou_d(plus)
        elif num3=='/':
            div=num1/num2
            print(div)
            lou_d(div)
        elif num3=='-':
            sub=num1-num2
            print(sub)
            lou_d(sub)
        elif num3=='%':
            per=num1%num2
            print(per)
            lou_d(per)
        else:
            print("error! please give correct option only")
            lou_d("error! please give correct option only")
        print("press C for Continue \npress E for Exit")
        lou_d("press c for continue or press e for exit")
        dec = input()
        if (dec=="c"):
            lou_d("Welcome back")
        elif(dec=="e"):
            lou_d("Thank you")
            break
if __name__ == '__main__':
    funct()