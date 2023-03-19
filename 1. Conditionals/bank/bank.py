greet = input("Greetings: ").lower().strip()
if greet.find("hello") == 0:
    print("$0")
elif greet.find("h") == 0:
    print("$20")
else:
    print("$100")