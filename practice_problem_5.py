'''
Author = Himanshu Bansal
Date = 7/5/2022
Purpose = practice problem
'''
def palidrome(i):
    while True:
        i = i+1
        ls = list(str(i))
        ls.reverse()
        if(ls==list(str(i))):
            z.append(str(i))
            break
        else:
            pass
if __name__ == '__main__':
    try:
        m = int(input("enter how many numbers you want in list :- "))
        t = []
        for i in range(m):
            s = int(input("enter the value :- "))
            t.append(s)
        print(f'The Given list is : {t}')
        z = []
        for i in t:
            if(i>10):
               palidrome(i)
            else:
                z.append(str(i))
        print(f'\n{z} : Only Greater Number then 10 got their next palidrome number.')

    except Exception as e:
        print("enter only valid input [integers only]")
