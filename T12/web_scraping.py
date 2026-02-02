import requests
from bs4 import BeautifulSoup
import csv
from collections import Counter
import matplotlib.pyplot as plt

# =========================
# 1. ACCESAREA PAGINII WEB
# =========================
URL = "https://www.bbc.com/news"

try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Eroare la accesarea site-ului:", e)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# =========================
# 2. EXTRAGEREA DATELOR
# =========================
articles = []

for item in soup.find_all("a", class_="gs-c-promo-heading"):
    title = item.get_text(strip=True)
    link = item.get("href")

    if link and link.startswith("/"):
        link = "https://www.bbc.com" + link

    summary_tag = item.find_next("p")
    summary = summary_tag.get_text(strip=True) if summary_tag else "Fara rezumat"

    category = "Altele"
    if "/business" in link:
        category = "Economie"
    elif "/technology" in link:
        category = "Tehnologie"
    elif "/world" in link:
        category = "Lume"

    articles.append({
        "Titlu": title,
        "Rezumat": summary,
        "URL": link,
        "Categorie": category
    })

print(f"Au fost extrase {len(articles)} articole.")

# =========================
# 3. SALVARE IN CSV
# =========================
with open("stiri_bbc.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["Titlu", "Rezumat", "URL", "Categorie"]
    )
    writer.writeheader()
    writer.writerows(articles)

print("Datele au fost salvate in stiri_bbc.csv")

# =========================
# 4. FILTRARE DUPA CUVANT CHEIE
# =========================
keyword = input("Introduceti un cuvant cheie pentru filtrare: ").lower()

print("\nArticole potrivite:")
for article in articles:
    if keyword in article["Titlu"].lower() or keyword in article["Rezumat"].lower():
        print(f"- {article['Titlu']} – {article['Rezumat']}")

# =========================
# 5. ANALIZA SI VIZUALIZARE
# =========================
categories = [article["Categorie"] for article in articles]
category_counts = Counter(categories)

plt.figure()
plt.bar(category_counts.keys(), category_counts.values())
plt.title("Distributia articolelor pe categorii")
plt.xlabel("Categorie")
plt.ylabel("Numar articole")
plt.show()
