def max_min(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num, min_num


try:
    input_list = input("Introduceti o lista de numere intregi separate prin virgula: ")

    num_list = [int(num.strip()) for num in input_list.split(',')]

    maximum, minimum = max_min(num_list)

    print(f"Maximul este: {maximum}")
    print(f"Minimul este: {minimum}")

except ValueError:
    print("Eroare: Introduceti doar numere intregi valide.")
