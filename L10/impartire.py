def imparte(a, b):
    try:
        rezultat = a / b
        return rezultat
    except ZeroDivisionError:
        return "Eroare: Nu se poate imparti la zero."
    except TypeError:
        return "Eroare: Argumentele trebuie sa fie numere."

print(imparte(10, 2))
print(imparte(10, 0))
print(imparte(10, "a"))