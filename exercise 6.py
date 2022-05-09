import random
print("\t\tSnake\t\tWater\t\tGun")
print("Rules :- ")
print("You Have to Win More Then 10 Times to be winner")
print("press Y to start the game ")
game=input()
lst = "s","w","g"
c=0
p=0
cp=0
if (game == "y"):
    print("\tS = SNAKE\n\tW = WATER\n\tG = GUN")
    while [()]:
        c=c+1
        player = input("Press any one of key to Play :-\n")
        com = random.choice(lst)
        if(c>10):
            print("Your score is ",p)
            print("Opponent score is ",cp)
            if(p>cp):
                print("You Are WINNER :)")
            elif(p<cp):
                print("You are LOOSER :(")
            else:
                print("ULTIMATE  DRAW :(")
            break
        elif(player =="s") and (com == "s"):
            print("Draw")
            print("Your score is ", p)
            print("Opponent score is ", cp)
        elif(player == "w") and (com=="w"):
            print("Draw")
            print("Your score is ", p)
            print("Opponent score is ", cp)
        elif(player =="g") and (com == "g"):
            print("Draw")
            print("Your score is ", p)
            print("Opponent score is ", cp)
        elif(player=="s") and (com =="w"):
            print("Winning shot")
            p=p+1
            print("Your score is ", p)
            print("Opponent score is ", cp)
        elif(player=="s") and (com=="g"):
            print("Looser")
            cp=cp+1
            print("Your score is ", p)
            print("Opponent score is ", cp)
        elif(player =="w") and (com=="s"):
            print("Looser")
            cp = cp + 1
            print("Your score is ", p)
            print("Opponent score is ", cp)
        elif(player=="w") and (com=="g"):
            print("Winning Shot")
            p = p + 1
            print("Your score is ", p)
            print("Opponent score is ", cp)
        elif(player=="g") and (com=="s"):
            print("Winning shot")
            p = p + 1
            print("Your score is ", p)
            print("Opponent score is ", cp)
        elif(player=="g") and (com=="w"):
            print("Looser")
            cp = cp + 1
            print("Your score is ", p)
            print("Opponent score is ", cp)
        else:
            print("Dont use other keys")
            continue
