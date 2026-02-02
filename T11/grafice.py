import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Exercitiul 1
np.random.seed(0)

dates_meteo = pd.date_range(start="2024-01-01", periods=365)

df_meteo = pd.DataFrame({
    "Data": dates_meteo,
    "Temperatura": np.random.uniform(5, 35, 365),
    "Umiditate": np.random.uniform(30, 90, 365),
    "Viteza Vantului": np.random.uniform(0, 20, 365)
})

df_meteo["Temperatura Resimtita"] = (
    df_meteo["Temperatura"] - 0.7 * (df_meteo["Umiditate"] / 100)
)

zi_max = df_meteo.loc[df_meteo["Temperatura Resimtita"].idxmax()]
zi_min = df_meteo.loc[df_meteo["Temperatura Resimtita"].idxmin()]

plt.figure()
plt.plot(df_meteo["Data"], df_meteo["Temperatura"], label="Temperatura")
plt.plot(df_meteo["Data"], df_meteo["Temperatura Resimtita"], label="Temperatura Resimtita")
plt.legend()
plt.xlabel("Data")
plt.ylabel("Grade Celsius")
plt.title("Temperatura vs Temperatura Resimtita")
plt.show()

df_meteo["Luna"] = df_meteo["Data"].dt.month
temp_medie_lunara = df_meteo.groupby("Luna")["Temperatura"].mean()

plt.figure()
temp_medie_lunara.plot(kind="bar")
plt.xlabel("Luna")
plt.ylabel("Temperatura Medie")
plt.title("Temperatura Medie Lunara")
plt.show()


# Exercitiul 2
np.random.seed(1)

dates_stock = pd.date_range(start="2023-01-01", periods=730)
returns = np.random.normal(0, 0.02, 730)
prices = 100 * np.cumprod(1 + returns)

df_stock = pd.DataFrame({
    "Data": dates_stock,
    "Schimbare Zilnica (%)": returns * 100,
    "Pret Inchidere": prices
})

df_stock["MA30"] = df_stock["Pret Inchidere"].rolling(30).mean()
df_stock["MA100"] = df_stock["Pret Inchidere"].rolling(100).mean()

plt.figure()
plt.plot(df_stock["Data"], df_stock["Pret Inchidere"], label="Pret Inchidere")
plt.plot(df_stock["Data"], df_stock["MA30"], label="MA30")
plt.plot(df_stock["Data"], df_stock["MA100"], label="MA100")
plt.legend()
plt.xlabel("Data")
plt.ylabel("Pret")
plt.title("Pret Actiune si Medii Mobile")
plt.show()

mask = df_stock["Pret Inchidere"] > df_stock["MA100"]

plt.figure()
plt.plot(df_stock.index, df_stock["Pret Inchidere"], label="Pret")
plt.plot(df_stock.index, df_stock["MA100"], label="MA100")
plt.fill_between(
    df_stock.index,
    df_stock["Pret Inchidere"].values,
    df_stock["MA100"].values,
    where=mask.fillna(False).values,
    alpha=0.3
)
plt.legend()
plt.xlabel("Zile")
plt.ylabel("Pret")
plt.title("Perioade peste Media Mobila 100")
plt.show()


# Exercitiul 3
np.random.seed(2)

df_ratings = pd.DataFrame({
    "ID Utilizator": np.random.randint(1, 1001, 10000),
    "ID Film": np.random.randint(1, 101, 10000),
    "Rating": np.random.randint(1, 6, 10000)
})

film_stats = df_ratings.groupby("ID Film").agg(
    Rating_Mediu=("Rating", "mean"),
    Numar_Evaluari=("Rating", "count")
)

top5 = film_stats.sort_values("Rating_Mediu", ascending=False).head(5)

filme_slabe = film_stats[
    (film_stats["Numar_Evaluari"] > 50) &
    (film_stats["Rating_Mediu"] < 3.5)
]

plt.figure()
plt.hist(df_ratings["Rating"])
plt.xlabel("Rating")
plt.ylabel("Frecventa")
plt.title("Distributia Ratingurilor")
plt.show()

plt.figure()
top5["Rating_Mediu"].plot(kind="bar")
plt.xlabel("ID Film")
plt.ylabel("Rating Mediu")
plt.title("Top 5 Filme cu Rating Mediu Maxim")
plt.show()

plt.figure()
plt.scatter(film_stats["Numar_Evaluari"], film_stats["Rating_Mediu"])
plt.xlabel("Numar Evaluari")
plt.ylabel("Rating Mediu")
plt.title("Numar Evaluari vs Rating Mediu")
plt.show()
