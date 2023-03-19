def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    return print(convert(input()))

main()