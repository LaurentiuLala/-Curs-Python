def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Eroare: Fișierul '{filename}' nu a fost găsit.")
    except IOError:
        print(f"Eroare: Nu s-a putut citi fișierul '{filename}'.")
    except Exception as e:
        print(f"Eroare neașteptată: {e}")

print (count_words_in_file("test.txt"));