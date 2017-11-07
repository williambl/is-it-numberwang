import random

def determine_numberwang(number, chance):
    for x in range(1,3):
        if (random.random() < chance):
            return True;
        else:
            return False;

def populate_numberwang_array():
    array = []
    for i in range(random.randrange(10,20)):
        # add between 10 and 20 values to the numberwang array
        if (random.random() < 0.3):
            array += [float(random.randrange(-1020,5000)/100)]
        else:
            array += [random.randrange(-102,500)]
    return array

if (__name__ == "__main__"):
    points = 0;
    numberwang_array = []

    for i in range(1,4): # Three rounds
        print("Round " + str(i) + ":")

        numberwang_array = populate_numberwang_array()
        print(numberwang_array)

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

        numberwang_array = populate_numberwang_array()
        print(numberwang_array)

        for j in range(0,5): # 5 chances
            if (determine_numberwang(float(input("> ")), 1.0/(i*2))):
                points += 1
                print("That's WangerNumb!")
            else:
                print("That's not WangerNumb.")
    print("\nYou got " + str(points) + " points!")
