def suma_din_fisier(nume_fisier):
    suma = 0
    try:
        with open(nume_fisier, "r") as fisier:
            for linie in fisier:
                try:
                    numar = float(linie.strip())
                    suma += numar
                except ValueError:
                    print(f"Valoare invalida ignorata: {linie.strip()}")
        return suma

    except FileNotFoundError:
        return "Eroare: Fisierul nu exista."
    except IOError:
        return "Eroare: Eroare la citirea fisierului."

rezultat = suma_din_fisier("numere.txt")
print(rezultat)