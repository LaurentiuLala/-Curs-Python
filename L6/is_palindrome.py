def is_palindrome(text):
    try:
        # Verificam daca inputul este string
        if not isinstance(text, str):
            raise TypeError("Inputul trebuie sa fie un sir de caractere (string).")

        # Eliminam spatiile si transformam in litere mici
        cleaned_text = "".join(text.lower().split())

        # Verificam daca este palindrom
        return cleaned_text == cleaned_text[::-1]

    except TypeError as e:
        print(f"Eroare de tip: {e}")
        return False
    except Exception as e:
        print(f"Eroare neasteptata: {e}")
        return False


# Exemplu
print(is_palindrome("A man a plan a canal Panama"))  # True

