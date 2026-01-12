# 1. Date de intrare
preturi = {
    "mere": 1.0,
    "banane": 0.5,
    "portocale": 0.8,
    "mango": 1.5
}

stoc_initial = {
    "mere": 10,
    "banane": 20,
    "portocale": 15,
    "mango": 5
}

vanzari = [
    ("mere", 4),
    ("banane", 6),
    ("portocale", 10),
    ("mango", 2)
]

# 2. Procesarea vanzarilor
venit_total = 0.0
stocuri = stoc_initial.copy()  # pentru a nu modifica stocul initial

for produs, cantitate in vanzari:
    if produs in preturi and produs in stocuri:
        venit_total += preturi[produs] * cantitate
        stocuri[produs] -= cantitate

# 3. Identificarea produselor ce necesita realimentare
produse_realimentare = {
    produs for produs, cantitate in stocuri.items() if cantitate < 5
}

# 4. Generarea raportului
print(f"Venit total: {venit_total} RON")
print("Stocuri ramase:")
for produs, cantitate in stocuri.items():
    print(f"  - {produs}: {cantitate}")

print("Produse ce necesita realimentare:")
for produs in produse_realimentare:
    print(f"  - {produs}")
