def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(percentage)
            break
        except:
            pass


def convert(fraction):
    l = fraction.split("/")
    x = int(l[0])
    y = int(l[1])
    if x > y:
        raise ValueError
    return round((x*100)/y)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
