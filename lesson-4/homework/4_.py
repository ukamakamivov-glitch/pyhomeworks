import random

#m = int(input("Enter a number: "))
n = random.randint(1,100)

i =0
yep = ['Y','YES', 'y','yes','ok']
while i != 10:
    m = int(input("Enter a number: "))

    i += 1
    if n == m:
        print("You guessed it right!")
        break

    elif n < m:
        print("Too high!")
        if i >= 10:
            c = input("You lost. Want to play again? ")
            if c in yep:
                i = 0
                n = random.randint(1, 100)
    elif n > m:
        print("Too low!")
        if i >= 10:
            c = input("You lost. Want to play again? ")
            if c in yep:
                i = 0
                n = random.randint(1, 100)


