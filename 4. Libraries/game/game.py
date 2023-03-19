from random import randint

while True:
    try:
        n = int(input("Level: "))
        assert n > 0
        break
    except:
        pass

r = randint(1, n)

while True:
    try:
        g = int(input("Guess: "))
        assert g > 0
        if g < r:
            print("Too small!")
        if g > r:
            print("Too large!")
        if g == r:
            print("Just right!")
            break
    except:
        pass