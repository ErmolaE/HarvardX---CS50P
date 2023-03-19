menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

amount = 0
while True:
    try:
        item = input("Order: ").lower().title()
        assert item in menu
        amount += menu[item]
        print(f"Total: ${amount:.2f}")
    except EOFError:
        break
    except AssertionError:
        pass
