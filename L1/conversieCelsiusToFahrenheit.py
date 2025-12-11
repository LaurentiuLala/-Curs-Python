try:
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"Fahrenheit: {fahrenheit}")
except ValueError:
    print("Eroare: Introduceti un numar valid.")