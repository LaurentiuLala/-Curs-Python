import math_operations as mo

try:
    a = 10
    b = 5

    print("Adunare:", mo.add(a, b))
    print("Scadere:", mo.subtract(a, b))
    print("Inmultire:", mo.multiply(a, b))
    print("Impartire:", mo.divide(a, b))

except ZeroDivisionError as zde:
    print("Eroare:", zde)

except Exception as e:
    print("Eroare neasteptata:", e)
