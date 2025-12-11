num = int(input("Introduceti un numar: "))

if num < 2:
    print("Numarul NU este prim.")
else:
    este_prim = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            este_prim = False
            break

    if este_prim:
        print("Numarul este prim.")
    else:
        print("Numarul NU este prim.")
