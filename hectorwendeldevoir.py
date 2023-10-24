import os
import time
import random
nbr = 0
while nbr < 5:
    tan_obje = 0
    pozisyon_aktyel = 1
    pozisyon = random.randint(0, 9)
    for tan_obje in range(9):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(9):
            if i == 9 or i==0:
                for j in range(9):
                    print("_ ", end="")
            if (i != 0 or i != 9):
                for j in range(8):
                    if j != pozisyon and i != pozisyon_aktyel:
                        print("  ", end="")
                    if j == pozisyon or i == pozisyon_aktyel:
                        if (i != pozisyon_aktyel or j != pozisyon):
                            print("  ", end="")
                        else:
                            print("M ", end="")
                print()
        pozisyon_aktyel += 1
        time.sleep(1/3)
        tan_obje += 1

