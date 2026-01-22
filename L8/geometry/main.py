from circle import area as circle_area, circumference
from rectangle import area as rectangle_area, perimeter

try:
    print("Aria cercului:", circle_area(5))
    print("Circumferinta cercului:", circumference(5))

    print("Aria dreptunghiului:", rectangle_area(4, 6))
    print("Perimetrul dreptunghiului:", perimeter(4, 6))

except ValueError as ve:
    print("Eroare de valoare:", ve)

except Exception as e:
    print("Eroare neasteptata:", e)
