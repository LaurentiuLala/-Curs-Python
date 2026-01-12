import string

def word_frequency(text):
    try:
        # Verificam daca inputul este string
        if not isinstance(text, str):
            raise TypeError("Inputul trebuie sa fie un sir de caractere (string).")

        text = text.lower()

        # Eliminam semnele de punctuatie
        for punct in string.punctuation:
            text = text.replace(punct, "")

        words = text.split()
        freq = {}

        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        return freq

    except TypeError as e:
        print(f"Eroare de tip: {e}")
        return {}
    except Exception as e:
        print(f"Eroare neasteptata: {e}")
        return {}


text = "Ana si Maria au plecat la mare. Maria are rau de mare."
print(word_frequency(text))
