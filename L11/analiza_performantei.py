import numpy as np
import pandas as pd

np.random.seed(42)

zile = pd.date_range(start="2024-01-01", periods=60)
produse = ["Laptop", "Telefon", "Tableta", "Monitor", "Casti"]

date = []

for zi in zile:
    nr_produse = np.random.randint(5, 16)

    for _ in range(nr_produse):
        produs = np.random.choice(produse)

        pret = np.random.normal(loc=40, scale=8)
        pret = max(10, pret)  # evitam preturi negative

        cantitate = np.random.randint(1, 11)

        promotie = np.random.rand() < 0.3
        if promotie:
            pret *= 0.8  # reducere 20%

        venit = pret * cantitate
        profit = venit * 0.30  # marja 30%

        date.append([zi, produs, pret, cantitate, promotie, venit, profit])

df_sim = pd.DataFrame(
    date,
    columns=["data", "produs", "pret", "cantitate", "promotie", "venit", "profit"]
)
zilnic = (
    df_sim.groupby("data")[["venit", "profit"]]
          .sum()
          .reset_index()
)

print(zilnic.head())
statistici = df_sim[["pret", "cantitate", "profit"]].agg(
    ["mean", "max", "min"]
)


venit_zilnic = zilnic["venit"]
profit_zilnic = zilnic["profit"]
zile = zilnic["data"]

distributie_pret = df_sim["pret"]
distributie_cantitate = df_sim["cantitate"]

promotii = df_sim[df_sim["promotie"] == True]

impact_promotii = promotii.groupby("data")["pret"].mean().reset_index()

print(impact_promotii.head())

pret_mediu = df_sim.groupby("promotie")["pret"].mean()
print(pret_mediu)
