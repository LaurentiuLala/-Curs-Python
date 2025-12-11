try:
    scor = float(input("Introduceti scorul (0-100): "))

    if scor < 0 or scor > 100:
        print("Eroare: Scorul trebuie sa fie intre 0 si 100.")
    elif scor >= 90:
        print("Nota A")
    elif scor >= 80:
        print("Nota B")
    elif scor >= 70:
        print("Nota C")
    elif scor >= 60:
        print("Nota D")
    else:
        print("Nota F")
except ValueError:
    print("Eroare: Introduceti un numar valid.")