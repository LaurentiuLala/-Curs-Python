import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

COINGECKO_URL = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin,ethereum&vs_currencies=usd"
)
COINDESK_URL = "https://www.coindesk.com/"

def get_crypto_prices():
    try:
        response = requests.get(COINGECKO_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Eroare la accesarea CoinGecko:", e)
        return None

def display_prices(prices):
    table = [
        ["Bitcoin", prices["bitcoin"]["usd"]],
        ["Ethereum", prices["ethereum"]["usd"]]
    ]

    print("\nPreturi criptomonede:\n")
    print(tabulate(table, headers=["Moneda", "Pret (USD)"], tablefmt="grid"))

def get_crypto_news():
    try:
        response = requests.get(COINDESK_URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        articles = soup.find_all("a", href=True)

        news = []
        for article in articles:
            title = article.get_text(strip=True)
            link = article["href"]

            if title and link.startswith("https://www.coindesk.com") and len(news) < 5:
                news.append((title, link))

        return news

    except requests.exceptions.RequestException as e:
        print("Eroare la accesarea CoinDesk:", e)
        return []

def display_news(news):
    print("\nUltimele 5 stiri crypto:\n")
    for idx, (title, link) in enumerate(news, start=1):
        print(f"{idx}. {title}")
        print(f"   {link}\n")

def main():
    prices = get_crypto_prices()
    if prices:
        display_prices(prices)

    news = get_crypto_news()
    if news:
        display_news(news)

if __name__ == "__main__":
    main()
