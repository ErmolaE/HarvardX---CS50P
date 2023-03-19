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
        if digit_valid(s):
            for i in range(len(s)):
                if s[i].isdigit():
                    if s[i] == "0":
                        return False
                    t=i
                    break
            for c in s[t:]:
                if c.isdigit() != True:
                    return False
        else:
            return True
    return True

def digit_valid(text):
    for c in text:
        if c.isalpha() != True:
            return True
    return False

main()