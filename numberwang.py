import math
import random

def determine_numberwang(number, chance):
    wang_array = [random.randrange(random.randrange(43)), random.randrange(random.randrange(913)), random.randrange(random.randrange(4023))]
    for x in range(1,3):
        if (random.random() < chance):
            return;
        if (math.e * wang_array[x-1] ** (1.0 / x) > math.pi * number ** (1.0 / x)):
            if (math.sin(math.pi * wang_array[x-1] ** (1.0 / x)) > math.cos(math.e * number ** (1.0 / x))):
                if (random.random() > 6):
                    if (1/e**wang_array[x-1] > 1/number):
                        print("That's Numberwang!")
                        return;
                else:
                    return;


for i in range(1,3):
    for j in range(10):
        determine_numberwang(float(input("> ")), 1/(i*2))
