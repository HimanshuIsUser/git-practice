import random
lst = 1,2,3,4,5,6,7,8,9,10
print("Hello Friends :)\n\nWELCOME TO THE LUCK GAME\n")
print("Enter the your Name for first player:-")
letter1=input()
print("Enter the your Name for second player :-")
letter2=input()
print("\nFirst player is:-",letter1 +"\n\nSecond player is:-",letter2)
print("\nThere are some rules given below please dont read them :)\n\n")
print("This is luck GAME so here we gone PLAY with your LUCK and our NUMBERS\nFor win this game you have to bring higher numbers then your opponent")
print("Both player has three chances to role the dice \nAfter all chances the number will added and the higher number will win this game ")
print("\n\nSo Be With Higher Number")
print("game starts now :-")
f=input(letter1 +" enter the roll to get your number")
if(f=="roll"):
    dice=random.choice(lst)
    print(dice)
    dice2 = random.choice(lst)
    print(dice2)
    dice3 = random.choice(lst)
    print(dice3)
else:
    print("try again")
print(letter2 +" enter the roll for your numbers")
f2=input()
if(f2=="roll"):
    chance=random.choice(lst)
    print(chance)
    chance2 = random.choice(lst)
    print(chance2)
    chance3=random.choice(lst)
    print(chance3)
else:
    print("try again")

sumo=dice+dice2+dice3

sumo2=chance+chance2+chance3

if(sumo>sumo2):
    print("WINNER IS "+letter1)
elif(sumo<sumo2):
    print("WINNER IS "+letter2)
else:
    print("D R A W ")
    print("BOTH TEAM HAVE EQUAL SCORE")
































































