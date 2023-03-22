import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
        numbers = ip.split(".")
        for number in numbers:
            if int(number) > 255:
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()