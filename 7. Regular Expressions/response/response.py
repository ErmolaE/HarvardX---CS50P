from validator_collection import checkers



def main():
    print(check(input("email: ")))


def check(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"




if __name__ == "__main__":
    main()