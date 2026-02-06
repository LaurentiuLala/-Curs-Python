import requests

# Citire date de la utilizator
moneda_sursa = input("Introdu moneda de provenienta (ex: EUR): ").upper()
moneda_destinatie = input("Introdu moneda de destinatie (ex: RON): ").upper()
suma = float(input("Introdu suma de convertit: "))

# API URL
url = f"https://api.exchangerate-api.com/v4/latest/{moneda_sursa}"

response = requests.get(url)
data = response.json()

# Obtine cursul de schimb
curs = data["rates"].get(moneda_destinatie)

if curs is None:
    print("Moneda introdusa nu este valida.")
else:
    suma_convertita = suma * curs

    print(f"\nSuma initiala: {suma} {moneda_sursa}")
    print(f"Curs de schimb: 1 {moneda_sursa} = {curs} {moneda_destinatie}")
    print(f"Suma finala: {suma_convertita:.2f} {moneda_destinatie}")
