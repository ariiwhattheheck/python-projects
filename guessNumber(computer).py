import random

def guessNumber(x):
    rand_num=random.randint(1,x)
    guess=0
    while guess!=rand_num:
        guess=int(input(f"""Enter a number between 1 and {x}: """))
        if guess <rand_num:
            print("Too low, try again")
        elif guess >rand_num:
            print("Too high, try again")

    print(f"""{rand_num}!!! DAANGGGG CORRECT GUESS""")

guessNumber(50)
         
