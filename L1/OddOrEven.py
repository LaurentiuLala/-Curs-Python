try:
    num = int(input("Introduceti numarul: "))
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
except ValueError:
    print("Eroare: Introduceti un numar valid")