# list comprehension :- help us to loop fun_tn in one line
# f=["harry" for i in range(1)]
# g=f.__iter__()
# print(g.__next__())
#..................................................................................
#dictnary comprenhension :- this help us to write the dictnary loop in one line .
# dic_t = {i:f"item{i}" for i in range(11) if i %2==0}
# dic_t2 = {value:key for key,value in dic_t.items()}
# print(dic_t)
# print("\n",dic_t2)
#....................................................................................
# #generators comprehension:-
# set_cpm = (i for i in range(100) )
# print(type(set_cpm))
# loop = set_cpm.__next__()
# for item in set_cpm:
#     print(item)
#........................................................................................
#set comprehension :-
# det_stp = {dress for dress in ("dress","dress2","dress3","dress4","dress1","dress2","dress3","dress4")}
# print(type(det_stp))
# print(det_stp)
#.........................................................
#exercise :-
print("enter how many inputs you want to enter")
no_of_input = input()
ty_in = input("enter the type of input")
if(ty_in == "list"):
    lis_t = [input("enter your input") for i in range(int(no_of_input))]
    print(lis_t)
elif(ty_in =="dict"):
    dict_nry ={input("key = "):input("value = ")for i in range(int(no_of_input))}
    print(dict_nry)
elif(ty_in =="set"):
    set_co = {input(":-") for i in range(int(no_of_input))}
    print(set_co)
    print(type(set_co))