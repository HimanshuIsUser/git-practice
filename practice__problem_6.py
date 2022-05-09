if __name__ == '__main__':
    while True:
        try:
            import random
            a = int(input("Enter the A value :- "))
            b = int(input("Enter the B value :- "))
            t = random.randint(a,b)
            print("The one number is already taken as guessing number \nyou have to find the number :\nTip :- Guessing number comes between a and b value")
            #player:
            player1 = input("First Player\t:\t")
            n=0
            while True:
                guess = int(input("Enter Number\t:\t"))
                n=n+1
                if(guess ==t):
                    print(f'\n CONGRATULATIONS {player1} you got the answer {t} in just {n} chances')
                    break
                elif(guess>t):
                    print(f'this one is greater then number\nNo of chances is {n}')
                elif (guess<t):
                    print(f'This one is smaller then number\nNo of chances is {n}')
            #player2 :
            player2 = input("Second Player\t:\t")
            p = 0
            t = random.randint(a, b)
            while True:
                p = p+1
                guess2 = int(input("Enter Number\t:\t"))
                if(guess2==t):
                    print(f'CONGRATULATIONS {player2} you got the answer {t} in {p} chances')
                    break

                elif(guess2>t):
                    print(f'this one is greater then number\nNo of chances is {p}')
                elif(guess2<t):
                    print(f'This one is smaller then number\nNo of chances is {p}')
            #RESULT:
            if(n<p):
                print(f'\n***********CONGRATULATIONS***********\n       {player1} You Are The Winner {n}        ')
            elif(n>p):
                print(f'\n***********CONGRATULATIONS***********\n       {player2} You Are The Winner {p}        ')
            else:
                print(f'You both have tough game and have similier score:\n{player1}\t:\t{t} no of chances you take\n{player2}\t:\t{p} no of chances you take')
            break
        except Exception as e:
            print("please enter only valid input")


