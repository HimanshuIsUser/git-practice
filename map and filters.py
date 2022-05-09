# a=0
# for i in range(10):
#     a=a+1
#     print(a)
# num = [1,2,3,4,5,6,7,8]
# sq = list(map(lambda x:x*x,num))
# print(sq)
#...........................................................
# number = ["1","2","4"]
# number=list(map(int,number))
# print(number)
# number[2]=number[2]+1
# print(number[2])
#............................................................
# def square(a):
#     return a*a
# def cube(a ):
#     return a*a*a
# fucn = [square,cube]
# for i in range(5):
#     val=list(map(lambda x:x(i),fucn))
#     print(val)
#.............................................................
#
# lst2= 2,3,4,5,6,7,8,9,
# def is_greater_5(num):
#     return num>5
# gr_than_5= list(filter(is_greater_5,lst2))  #list convert tuple objects into integers
# print(gr_than_5)
#...............................................................
from functools import reduce
lst=1,2,3,4,5,6,76
val=reduce(lambda x,y:x+y,lst)
print(val)
print(sum(lst))
