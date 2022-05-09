# n = int(input("enter the no of Apple's harry have :- "))
# mn  =int(input("enter minimum number of students :- "))
# mx  = int(input("enter the maximum number of students :- "))
n = int(input())
# mn = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# t = mn.insert(1,34)
# for num in mn:
    # if n%int(num)==0:
        # print(num)
mx = int(input("enter your maximum value :- "))
mn = int(input("enter the your minimum value :- "))
for i in range(mx):
    mn = mn+1
    new = int(mn)
    if (mn>mx):
        break
    elif(mn==mx):
        if(n%mn==0):
            print(f'{n} apples will be possible to distribute equally {new} students')
    elif(n%mn==0):
        print(f'{n} Apples will be possible to distribute equally {new} students')
    else:
        print(f'{n} Apples cannot be possible to distribute equally {new} students')


