try:
    input_values = input("Introduceti valori separate prin virgula: ")
    my_tuple = tuple(int(x.strip()) for x in input_values.split(','))

    search_value = int(input("Cautati valoarea: "))

    print(f"Tupla: {my_tuple}")

    if search_value in my_tuple:
        index = my_tuple.index(search_value)
        print(f"{search_value} se regaseste in tupla la indexul {index}.")
    else:
        print(f"{search_value} nu se regaseste in tupla.")

except ValueError:
    print("Eroare: Introduceti doar numere intregi valide.")
