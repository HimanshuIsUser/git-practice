def funt(n):
    dup = str(n)[:]
    while True:
        n = n + 1
        t = list(str(n))
        t.reverse()
        if (t == list(str(n))):
            with open("palidrome_no.txt",'a')as p:
                p.write(f'{n} is a palindrome  number of {dup}\n')
            break
        else:
            pass

try:
    times = int(input("enter how many numbers you want to input :- "))
    for i in range(times):
        n = int(input("enter the number :- "))
        funt(n)
    with open("palidrome_no.txt",'r')as p:
        print(p.read())
except Exception as e:
    print("Please Enter only intigers")
