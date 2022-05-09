# def shu(a):
#     return a[1]
#
a = [[1,5],[2,3],[8,5],[5,1]]
#
# a.sort(key=shu)
# print(a)
a.sort(key=lambda x:x[1])
print(a)
