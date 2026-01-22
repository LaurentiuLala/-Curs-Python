import math

try:
    num = 25
    angle = 30

    if num < 0:
        raise ValueError("Numarul trebuie sa fie pozitiv pentru radical.")

    sqrt_result = math.sqrt(num)
    factorial_result = math.factorial(num)
    sin_result = math.sin(math.radians(angle))

    print(f"Radacina patrata a {num} este {sqrt_result}")
    print(f"Factorialul lui {num} este {factorial_result}")
    print(f"Sinusul unghiului de {angle} grade este {sin_result}")

except ValueError as ve:
    print("Eroare de valoare:", ve)

except Exception as e:
    print("Eroare neasteptata:", e)
