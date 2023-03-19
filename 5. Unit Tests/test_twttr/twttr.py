def main():
    s = input("Text: ")
    print(shorten(s))


def shorten(word):
    return ''.join([c for c in word if c not in 'aeiouAEIOU'])


if __name__ == "__main__":
    main()

