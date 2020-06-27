import sys
import random
magic = input("ask a question to magic ball (type q to exit) : ")
rand = random.randint(1, 4)
if magic == "q":
    sys.exit()
elif rand == 1:
    print("It is certain")
elif rand == 2:
    print("Outlook good")
elif rand == 3:
    print("ask again later")
