import random

secret_number = random.randint(0, 9)
tries = 0
while tries < 4:
    num = int(input("Guess the number between 0 and 9: "))
    tries += 1
    if num == secret_number:
        print("Yaay you picked the right number you win")
        break
    elif num != secret_number and tries != 4:
        print("you picked the wrong number pick again")
else:
    print(f"You loose, the number is {secret_number}")
