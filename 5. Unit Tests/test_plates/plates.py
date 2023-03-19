def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    t=0
    if len(s)>6 or len(s)<2:
        return False
    elif s.isalnum() != True:
        return False
    elif s[0:1].isalpha() != True:
        return False
    elif len(s)>2:
        for c in s:
            if c.isalpha() != True:
                for i in range(len(s)):
                    if s[i].isdigit():
                        if s[i] == "0":
                            return False
                        t=i
                        break
                for c in s[t:]:
                    if c.isdigit() != True:
                        return False
                break
    return True

if __name__ == "__main__":
    main()