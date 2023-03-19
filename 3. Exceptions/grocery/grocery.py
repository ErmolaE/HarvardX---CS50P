d = {}
while True:
    try:
        item = input()
        item = item.upper()
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    except EOFError:
        sort_d = dict(sorted(d.items()))
        for item in sort_d:
            print(f"{d[item]} {item}")
        break
