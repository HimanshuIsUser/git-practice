lst = "himanshu","mohan","manish","gourav","kd","javed"

# i=1
# for items in lst:
#     if i%2!=0:
#         print(items)
#     i=i+1
# .............................................................................
# a given for import in another file for practice . but for this programe just ignore it
a=45
print("the name of this is",__name__)
# if __name__ == '__main__':
def add(num1,num2):
    return num1+num2+5
if __name__ == '__main__':
# .........................................................................................
    for index,items in enumerate(lst):
        if index%2==0:
            print(items)
    # print(add(5,17))