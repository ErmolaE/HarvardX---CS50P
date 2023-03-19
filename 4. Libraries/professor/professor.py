import random

def main():
    level = get_level()
    score = 0
    t = 0
    for i in range(10):
        x, y = generate_integer(level)
        right_answer = x + y
        while True:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                assert user_answer == right_answer
                score += 1
                break
            except:
                print("EEE")
                t += 1
                if t == 3:
                    print(f"{x} + {y} = {right_answer}")
                    t = 0
                    break
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            assert 0 < n <= 3
            return n
        except:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    if level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    if level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
