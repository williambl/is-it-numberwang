import math
import random

def determine_numberwang(number, chance):
    wang_array = [random.randrange(random.randrange(43)), random.randrange(random.randrange(913)), random.randrange(random.randrange(4023))]
    for x in range(1,3):
        if (random.random() < chance):
            return False;
        if (math.e * wang_array[x-1] ** (1.0 / x) > math.pi * number ** (1.0 / x)):
            if (math.sin(math.pi * wang_array[x-1] ** (1.0 / x)) > math.cos(math.e * number ** (1.0 / x))):
                if (random.random() > 6):
                    if (1/e**wang_array[x-1] > 1/number):
                        return True;
                else:
                    return True;
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
                poits += 1
                print("That's WangerNumb!")
            else:
                print("That's not WangerNumb.")
    print("\nYou got " + str(points) + " points!")
