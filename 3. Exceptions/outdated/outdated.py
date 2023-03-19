months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()
        if date.find("/") != -1:
            l = date.split("/")
            l[0] = int(l[0])
            l[1] = int(l[1])
        elif date.find(" ") != -1:
            l = date.split()
            l[0] = months.index(l[0]) + 1
            l[1] = int(l[1][:len(l[1])-1])
        else:
            continue
        assert l[0] <= 12
        assert l[1] <= 31
        print(f"{l[2]}-{l[0]:02}-{l[1]:02}")
        break
    except:
        pass