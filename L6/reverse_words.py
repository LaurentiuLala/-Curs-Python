def reverse_words(sentence):
    try:
        # Verificam daca inputul este string
        if not isinstance(sentence, str):
            raise TypeError("Inputul trebuie sa fie un sir de caractere (string).")

        # Eliminam spatiile suplimentare si impartim in cuvinte
        words = sentence.split()

        # Inversam ordinea cuvintelor
        reversed_words = words[::-1]

        # Refacem propozitia
        return " ".join(reversed_words)

    except TypeError as e:
        print(f"Eroare de tip: {e}")
        return ""
    except Exception as e:
        print(f"Eroare neasteptata: {e}")
        return ""


# Exemplu
sentence = "soricel   un cu   joaca se pisica"
print(reverse_words(sentence))
