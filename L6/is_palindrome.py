def is_palindrome(text):
    # Eliminam spatiile si transformam in litere mici
    cleaned_text = "".join(text.lower().split())
    # Verificam daca este palindrom
    return cleaned_text == cleaned_text[::-1]


# Exemplu
text = "A man a plan a canal Panama"
print(is_palindrome(text))

