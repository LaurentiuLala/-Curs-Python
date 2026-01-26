def adauga_produs(inventar, nume, cantitate):
    if not isinstance(cantitate, int) or cantitate < 0:
        raise ValueError("Cantitatea trebuie sa fie un numar intreg pozitiv.")
    inventar[nume] = cantitate


def cauta_produs(inventar, nume):
    try:
        return inventar[nume]
    except KeyError:
        raise KeyError("Produsul nu exista in inventar.")


def actualizeaza_cantitate(inventar, nume, cantitate):
    if nume not in inventar:
        raise KeyError("Produsul nu exista.")
    if not isinstance(cantitate, int) or cantitate < 0:
        raise ValueError("Cantitatea trebuie sa fie un numar intreg pozitiv.")
    inventar[nume] = cantitate


def main():
    inventar = {}

    try:
        adauga_produs(inventar, "Laptop", 10)
        adauga_produs(inventar, "Mouse", 25)

        print("Cantitate Laptop:", cauta_produs(inventar, "Laptop"))

        actualizeaza_cantitate(inventar, "Laptop", 15)
        print("Cantitate Laptop actualizata:", cauta_produs(inventar, "Laptop"))

        # Produs inexistent
        print(cauta_produs(inventar, "Tastatura"))

    except ValueError as e:
        print("Eroare:", e)
    except KeyError as e:
        print("Eroare:", e)


main()
