import random

def guessNum(x):
    low=0
    high=x
    feedback=''

    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low

        feedback=input(f"""Is {guess} correct(C), high(H) or low(L): """).lower()

        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1

    print(f"""LMFAO BOZO00 computer guessed ur number {guess}""")

guessNum(20)
            
