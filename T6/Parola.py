def verifica_parola(parola):
    criterii_neindeplinite = []

    caractere_speciale = "!@#$%^&*()-_+=<>?"

    # Lungime minima
    if len(parola) < 8:
        criterii_neindeplinite.append("lungimea minima de 8 caractere")

    # Litera majuscula
    if not any(c.isupper() for c in parola):
        criterii_neindeplinite.append("o litera majuscula")

    # Litera minuscula
    if not any(c.islower() for c in parola):
        criterii_neindeplinite.append("o litera minuscula")

    # Cifra
    if not any(c.isdigit() for c in parola):
        criterii_neindeplinite.append("o cifra")

    # Caracter special
    if not any(c in caractere_speciale for c in parola):
        criterii_neindeplinite.append("un caracter special")

    # Fara spatii
    if " " in parola:
        criterii_neindeplinite.append("eliminarea spatiilor")

    return criterii_neindeplinite


# Program principal
input_parole = input("Introduceti parola/parolele (separate prin virgula): ")

parole = [p.strip() for p in input_parole.split(",")]

print("\nRezultate verificare parole:")
print("-" * 30)

for parola in parole:
    probleme = verifica_parola(parola)

    print(f"\nParola: '{parola}'")
    if not probleme:
        print("Parola dvs. este PUTERNICA.")
    else:
        print("Parola dvs. este SLABA.")
        print("Lipsesc urmatoarele criterii:")
        for problema in probleme:
            print(f"- {problema}")
