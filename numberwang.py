import random

def determine_numberwang(number, chance):
    for x in range(1,3):
        if (random.random() < chance):
            return True;
        else:
            return False;

if (__name__ == "__main__"):
    points = 0;

    for i in range(1,4): # Three rounds
        print("Round " + str(i) + ":")
        for j in range(0,5): # 5 chances
            if (determine_numberwang(float(input("> ")), 1.0/(i*2))):
                points += 1
                print("That's Numberwang!")
            else:
                print("That's not Numberwang.")
    # Wangernumb
    print("\nLet's Rotate the Board! It's time for WangerNumb!\n")
    for i in range(1,4): # Three rounds
        print("Round " + str(i) + ":")
        for j in range(0,5): # 5 chances
            if (determine_numberwang(float(input("> ")), 1.0/(i*2))):
                points += 1
                print("That's WangerNumb!")
            else:
                print("That's not WangerNumb.")
    print("\nYou got " + str(points) + " points!")
