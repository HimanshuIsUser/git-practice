import random
def rohanmultiplication(t):
    s = []
    n = random.randint(2,11)
    for i in range(1,11):
        j = random.randint(2,10)
        if(i==n):
            f = t*i+j
        else:
            f = t*i
        s.append(f)
    print(f'{s} this is rohan\'s programme')
    k = 0
    lst = []
    for i in s:
        k = k+1
        o = t*k
        index = []
        if (i==o):
            lst.append(i)
        else:
            lst.append(o)
    print(f'{lst} real')
    if(s==lst):
        print(f'both are equal :)')
    else:
        print(f'Error!\ncheck the index no {n} :( ')
if __name__ == '__main__':
    try:
        t = int(input("enter the value : "))
        rohanmultiplication(t)
    except Exception as e:
        print(e)