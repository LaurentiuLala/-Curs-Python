try:
    input_values = input("Introduceti o lista de numere separate prin virgula: ")
    numbers = [int(x.strip()) for x in input_values.split(',')]

    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    print("Lista fara duplicate:")
    print(", ".join(str(x) for x in unique_numbers))

except ValueError:
    print("Eroare: Introduceti doar numere intregi valide.")
