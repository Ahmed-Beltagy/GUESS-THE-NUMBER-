   # LEVEL 1 & 2 & 3
def Leve_One():
    print("Let's Start")
    print()
    import random
    attempts = 3
    n = random.randint(1, 10)
    x = str(n)
    while attempts > 0:
        if attempts == 0:
            break
        answer = int(input("*** please guess a number between 1 & 10 *** "))
        if answer == n:
            print()
            print("$$$ Gongratulations you got it right $$$")
            print()
            re_play = input("&&& Do you want to play again the same Level or you want another level( same \ another) or exit to quit....&&& ").lower()
            if re_play == "same":
                Leve_One()
            elif re_play == "another":
                Level_Selection()
            elif re_play == "exit":
                print("Thank You for Playing...")
                exit()

        else:
            print("Sorry you got it wrong")
            attempts = attempts - 1
            if attempts == 0:
                print("******************************GAME OVER! YOU LOSE****************************")
                re_play = input(
                    "&&& Do you want to play again the same Level or you want another level( same \ another) or exit to quit....&&&").lower()
                if re_play == "same":
                    Leve_One()
                elif re_play == "another":
                    Level_Selection()
                elif re_play == "exit":
                    print("Thank You for Playing....")
                    exit()
            else:
                print("continue you still have", attempts, "tries")
def Level_Two():
    print("Let's Start")
    print()
    import random
    attempts = 5
    hints = 1
    n = str(random.randint(10, 100))
    while attempts > 0:
        if attempts == 0:
            break
        answer = int(input("*** please guess a number between 10 & 100... ***  "))
        if answer == n:
            print()
            print("$$$ Gongratulations you got it right $$$")
            print()
            re_play = input("&&& Do you want to play again the same Level or you want another level( same \ another) or exit to quit....&&& ").lower()
            if re_play == "same":
                Level_Two()
            elif re_play == "another":
                Level_Selection()
            elif re_play == "exit":
                print("Thank You for Playing...")
                exit()

        else:
            print("Sorry you got it wrong")
            attempts = attempts - 1
            if hints != 0 and attempts != 0:
                hint = input("Do you want a hint.....").lower()
                if hint == "yes":
                    print("The first digit is:", n[0])
                    hints = hints - 1
            if attempts == 0:
                print()
                print("*************************GAME OVER************************************")
                print()
                re_play = input("&&& Do you want to play again the same Level or you want another level( same \ another) or exit to quit....&&& ").lower()
                if re_play == "same":
                    Level_Two()
                elif re_play == "another":
                    Level_Selection()
                elif re_play == "exit":
                    print("Thank You for Playing....")
                    exit()
            else:
                print("continue you still have", attempts, "tries")
def Leve_Three():
    print("Let's Start")
    print()
    import random
    hints = 1
    attempts = 7
    n = str(random.randint(100, 1000))
    # print(n)
    while attempts > 0:
        answer = int(input("*** please guess a number between 100 & 1000 ***  "))
        if answer == n:
            print()
            print("$$$ Gongratulations you got it right $$$")
            print()
            re_play = input("&&& Do you want to play again the same Level or you want another level( same \ another) or exit to quit....&&& ").lower()
            if re_play == "same":
                Leve_Three()
            elif re_play == "another":
                Level_Selection()
            elif re_play == "exit":
                print("Thank You for Playing...")
                exit()
        else:
            print("Sorry you got it wrong")
            attempts = attempts - 1
            if hints != 0 and attempts != 0:
                hint = input("Do you want a hint.....").lower()
                if hint == "yes":
                    print("The first digit is:", n[0])
                    hints = hints - 1
            if attempts == 0:
                print("**************************Game over! YOU LOSE******************************")
                re_play = input(
                    "&&& Do you want to play again the same Level or you want another level( same \ another) or exit to quit....&&&").lower()
                if re_play == "same":
                    Leve_Three()
                elif re_play == "another":
                    Level_Selection()
                elif re_play == "exit":
                    print("Thank You for Playing....")
                    exit()
            else:
                print("continue you still have", attempts, "tries")

                
# Introduction & Level Selection
def main():
    Name = input("Please enter your name  ")
    print()
    print("Hello,", Name, ",Welcome to GUESS THE NUMBER!!!")
    print()
    print("This is a guess game.")
    print()
    print("You have number of chances depends on the level you play to guess the answer right.")
    print()
    print("You will loose if you not guessed the right answer.")
    print()
    print("This game has three levels (Easy-Normal-Hard)")
    print()
def Level_Selection():
    print("1- Easy-> Guess number between 1 & 10 and you have 3 tries")
    print()
    print("2- Normal-> Guess number between 10 & 100 and you have 5 tries, and you have a hint to give you the first digit:")
    print()
    print("3- Hard-> Guess number between 100 & 1000 and you have 7 tries, and you have a hint to give you the first digit:")
    print()

    Level = int(input("please select your level..."))
    if Level == 1:
        Leve_One()
    elif Level == 2:
        Level_Two()
    elif Level == 3:
        Leve_Three()

main()
Level_Selection()

