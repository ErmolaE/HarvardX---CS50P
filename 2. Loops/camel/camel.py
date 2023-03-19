s = input("The name of a variable in camel case: ")
for c in s:
    if c.isupper():
        s=s.replace(c, "_" + c.lower())
print(s)