x, y, z = input("Expression: ").split(" ")
if y == "+":
    print(f"{(float(x)+float(z)):.1f}")
if y == "-":
    print(f"{(float(x)-float(z)):.1f}")
if y == "*":
    print(f"{(float(x)*float(z)):.1f}")
if y == "/":
    print(f"{(float(x)/float(z)):.1f}")