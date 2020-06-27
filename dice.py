import random
import sys
min = 1
max = 6
while True:
    ans = input("do you want to roll the dice?(y/n): ")
    if ans == 'yes' or ans == 'y' or ans == "YES" or ans == "Y":
        print("Random number: ", random.randint(min, max))
        pass
    elif ans == "no" or ans == "n" or ans == "NO" or ans == "N":
        print("Ok...bye")
        pass
    else:
        print("Invalid input")
        break
    print("The program is finished!!")
    sys.exit()

