while True:
    try:
        fraction = input("Fraction: ")
        l = fraction.split("/")
        x = int(l[0])
        y = int(l[1])
        assert x <= y
        percent = round((x*100)/y)
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{percent}%")
        break
    except:
        pass

