def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


cuvant = input("Introduceti un cuvant: ")

if is_palindrome(cuvant):
    print(f"'{cuvant}' este palindrom.")
else:
    print(f"'{cuvant}' nu este palindrom.")