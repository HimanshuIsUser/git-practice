f = input("Enter The Your Age Or Birth Year :- ")
if (int(f)<1500):
    rest = 100-int(f)
    rest2 = 2022-int(f)
    century = rest+2022
    print("your 100th age will be on this year :-",century)
    print("your birth year is :-",rest2)
    if int(f)>150:
        print("congratulations you are oldest person alive")
    year = input("Enter any Year :- ")
    if int(year)>int(rest2):
        century2 = int(year)-int(rest2)
        print(century2)
    elif int(year)<int(rest2):
        print("its too early , even you didn't get the birth")
elif(int(f)>1500):
    gap = 2022-int(f)
    gap2 = int(f)+100
    print("your Age is :-",gap)
    print("your 100th age will be on this Year :-",gap2)
    if int(gap)>150:
        print("congratulations you are oldest person alive :)")
    year = input("Enter the Year :- ")
    if int(year)>int(f):
        gap3 = int(year)-int(f)
        print(f'Your Age will be {gap3} in {year} Year')
    elif int(year)<int(f):
        print("take birth first :)")