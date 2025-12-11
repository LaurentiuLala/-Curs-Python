try:
    principal = float(input("Principal: "))
    rate = float(input("Rata anuala (%): "))
    time = float(input("Timp (ani): "))

    interest = (principal * rate * time) / 100
    print(f"Dobanda: {interest}")
except ValueError:
    print("Eroare: Introduceti un numar valid.")