FILE_NAME = "movies.txt"


def load_movies():
    movies = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file.readlines():
                title, rating = line.strip().split(", ")
                movies[title] = int(rating)
    except FileNotFoundError:
        print("Fișierul movies.txt nu există. Se va crea unul nou.")
    return movies


def save_movies(movies):
    with open(FILE_NAME, "w") as file:
        for title, rating in movies.items():
            file.write(f"{title}, {rating}\n")


def get_valid_rating():
    while True:
        try:
            rating = int(input("Introdu evaluarea (1-5): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Evaluarea trebuie să fie între 1 și 5.")
        except ValueError:
            print("Introdu un număr valid.")


def display_movies(movies):
    if not movies:
        print("Nu există filme în listă.")
        return

    print("\nFilme (sortate după evaluare):")
    for title, rating in sorted(movies.items(), key=lambda x: x[1], reverse=True):
        print(f"- {title}: {rating}")


def add_movie(movies):
    title = input("Introdu titlul filmului: ")
    if title in movies:
        print("Filmul există deja.")
        return
    rating = get_valid_rating()
    movies[title] = rating
    save_movies(movies)
    print("Film adăugat cu succes.")


def update_movie(movies):
    title = input("Introdu titlul filmului de actualizat: ")
    if title not in movies:
        print("Filmul nu există.")
        return
    rating = get_valid_rating()
    movies[title] = rating
    save_movies(movies)
    print("Evaluare actualizată.")


def delete_movie(movies):
    title = input("Introdu titlul filmului de șters: ")
    if title in movies:
        del movies[title]
        save_movies(movies)
        print("Film șters.")
    else:
        print("Filmul nu există.")


def main():
    movies = load_movies()

    while True:
        print("""
=== Sistem de Evaluare a Filmelor ===
1. Vizualizează filmele
2. Adaugă film
3. Actualizează evaluare
4. Șterge film
5. Salvează și ieși
""")

        choice = input("Alege o opțiune (1-5): ")

        if choice == "1":
            display_movies(movies)
        elif choice == "2":
            add_movie(movies)
        elif choice == "3":
            update_movie(movies)
        elif choice == "4":
            delete_movie(movies)
        elif choice == "5":
            save_movies(movies)
            print("Modificările au fost salvate. La revedere!")
            break
        else:
            print("Opțiune invalidă.")


if __name__ == "__main__":
    main()