import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()
        data = response.json()

        current = data["current_condition"][0]
        weather_desc = current["weatherDesc"][0]["value"]
        temperature = current["temp_C"]
        wind_speed = current["windspeedKmph"]
        wind_dir = current["winddir16Point"]

        print("\nInformatii meteo:")
        print(f"Oras: {city}")
        print(f"Conditii meteo: {weather_desc}")
        print(f"Temperatura: {temperature} °C")
        print(f"Vant: {wind_dir}, {wind_speed} km/h")

    except requests.exceptions.SSLError:
        print("Eroare SSL. Incercare fara verificarea certificatului...")
    except requests.exceptions.RequestException:
        print("Eroare la conectarea la API sau oras invalid.")
    except KeyError:
        print("Orasul nu a fost gasit.")

def main():
    city = input("Introdu numele orasului: ")
    get_weather(city)

if __name__ == "__main__":
    main()
