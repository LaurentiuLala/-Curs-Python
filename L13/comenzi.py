import csv

input_file = "comenzi.csv"
output_file = "rezultate_comenzi.csv"

with open(input_file, mode="r", newline="", encoding="utf-8") as infile, \
     open(output_file, mode="w", newline="", encoding="utf-8") as outfile:

    reader = csv.DictReader(infile)
    fieldnames = ["Produs", "Cantitate", "Pret unitar", "Valoare totala"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:
        cantitate = int(row["Cantitate"])
        pret_unitar = float(row["Pret unitar"])
        valoare_totala = cantitate * pret_unitar

        row["Valoare totala"] = valoare_totala
        writer.writerow(row)

print("Procesarea fisierului CSV a fost finalizata.")
