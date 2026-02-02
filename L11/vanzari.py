import pandas as pd

df = pd.read_csv("vanzari.csv")
df["data_vanzarii"] = pd.to_datetime(df["data_vanzarii"])

# venit per vânzare
df["venit"] = df["cantitate"] * df["pret"]
df["luna"] = df["data_vanzarii"].dt.to_period("M")

cele_mai_vandute = (
    df.groupby(["luna", "produs"])["cantitate"]
      .sum()
      .reset_index()
)

cele_mai_vandute = (
    cele_mai_vandute
    .sort_values(["luna", "cantitate"], ascending=[True, False])
)

print(cele_mai_vandute)
venit_per_produs = (
    df.groupby("produs")["venit"]
      .sum()
      .reset_index()
)

print(venit_per_produs)
start = "2024-01-01"
end = "2024-03-31"

df_interval = df[
    (df["data_vanzarii"] >= start) &
    (df["data_vanzarii"] <= end)
]

print(df_interval)
start = "2024-01-01"
end = "2024-03-31"

df_interval = df[
    (df["data_vanzarii"] >= start) &
    (df["data_vanzarii"] <= end)
]

print(df_interval)
