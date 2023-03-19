def main():
    greeting = input("Greetings: ").strip()
    value_print = value(greeting)
    print(f"${value_print}")


def value(greeting):
    greeting = greeting.lower()
    if greeting.find("hello") == 0:
        return 0
    elif greeting.find("h") == 0:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

