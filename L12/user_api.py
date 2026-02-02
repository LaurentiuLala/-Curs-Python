import requests
from tabulate import tabulate

URL = "https://jsonplaceholder.typicode.com/users"

def get_users():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Eroare la interogarea API-ului:", e)
        return None

def display_users(users):
    table = []
    for user in users:
        table.append([
            user["id"],
            user["name"],
            user["username"],
            user["email"],
            user["address"]["city"],
            user["company"]["name"],
            user["phone"],
            user["website"]
        ])

    headers = ["ID", "Name", "Username", "Email", "City", "Company", "Phone", "Website"]
    print(tabulate(table, headers=headers, tablefmt="grid"))

def filter_by_city(users, city):
    return [user for user in users if user["address"]["city"].lower() == city.lower()]

def main():
    users = get_users()
    if not users:
        return

    print("\n--- Lista completa utilizatori ---\n")
    display_users(users)

    city = "Gwenborough"
    filtered_users = filter_by_city(users, city)

    print(f"\n--- Utilizatori din orasul {city} ---\n")
    display_users(filtered_users)

if __name__ == "__main__":
    main()
