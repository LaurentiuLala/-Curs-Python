import string


def word_frequency(text):
    text = text.lower()

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



text = "Ana si Maria au plecat la mare. Maria are rau de mare."
print(word_frequency(text))
