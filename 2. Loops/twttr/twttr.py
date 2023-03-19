
def anti_vowel(s):
    return ''.join([c for c in s if c not in 'aeiouAEIOU'])

s = input("Text: ")
print(anti_vowel(s))