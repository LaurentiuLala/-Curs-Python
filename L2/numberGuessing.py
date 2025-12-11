import random

numar_secret = random.randint(1, 20)
incercari = 5
ghicit = False

print("Am ales un numar intre 1 si 20. Ai 5 incercari!")

while incercari > 0 and not ghicit:
    try:
        ghicire = int(input(f"Incercarea {6 - incercari}/5: "))

        if ghicire == numar_secret:
            print("Corect!")
            ghicit = True
        elif ghicire > numar_secret:
            print("Prea mare")
            incercari -= 1
        else:
            print("Prea mic")
            incercari -= 1
    except ValueError:
        print("Eroare: Introduceti un numar valid")

if not ghicit:
    print(f"Ai pierdut! Numarul era {numar_secret}.")