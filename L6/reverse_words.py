def reverse_words(sentence):
    # Eliminam spatiile suplimentare si impartim in cuvinte
    words = sentence.split()
    # Inversam ordinea cuvintelor
    reversed_words = words[::-1]
    # Refacem propozitia
    return " ".join(reversed_words)


# Exemplu
sentence = "soricel   un cu   joaca se pisica"
print(reverse_words(sentence))

