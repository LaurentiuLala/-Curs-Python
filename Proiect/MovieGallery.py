import tkinter as tk
from tkinter import messagebox

MOVIE_FILE = "movies.txt"

# ------------------ FILE HANDLING ------------------

def load_movies():
    movies = []
    try:
        with open(MOVIE_FILE, "r") as f:
            for line in f:
                title, year, genre, rating, desc = line.strip().split("|")
                movies.append({
                    "title": title,
                    "year": year,
                    "genre": genre,
                    "rating": rating,
                    "description": desc
                })
    except FileNotFoundError:
        pass
    return movies


def save_movies():
    with open(MOVIE_FILE, "w") as f:
        for m in movies:
            f.write(f"{m['title']}|{m['year']}|{m['genre']}|{m['rating']}|{m['description']}\n")


movies = load_movies()
current_role = None

# ------------------ LOGIN WINDOW ------------------

def open_login():
    def login(role):
        nonlocal login_window
        global current_role
        current_role = role
        login_window.destroy()
        open_main_app()

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("300x200")

    tk.Label(login_window, text="Select role", font=("Arial", 14)).pack(pady=20)

    tk.Button(login_window, text="Admin", width=15, command=lambda: login("admin")).pack(pady=5)
    tk.Button(login_window, text="User", width=15, command=lambda: login("user")).pack(pady=5)

    login_window.mainloop()

# ------------------ MAIN APP ------------------

def open_main_app():
    app = tk.Tk()
    app.title("🎬 Movie Gallery")
    app.geometry("800x400")

    left = tk.Frame(app)
    left.pack(side="left", fill="y", padx=10)

    right = tk.Frame(app)
    right.pack(side="right", fill="both", expand=True)

    listbox = tk.Listbox(left, width=30)
    listbox.pack(fill="y")

    def refresh_list():
        listbox.delete(0, tk.END)
        for m in movies:
            listbox.insert(tk.END, m["title"])

    refresh_list()

    title_lbl = tk.Label(right, text="", font=("Arial", 16, "bold"))
    title_lbl.pack(anchor="w")

    info_lbl = tk.Label(right)
    info_lbl.pack(anchor="w")

    desc_lbl = tk.Label(right, wraplength=400, justify="left")
    desc_lbl.pack(anchor="w", pady=10)

    def show_movie(event):
        if listbox.curselection():
            m = movies[listbox.curselection()[0]]
            title_lbl.config(text=m["title"])
            info_lbl.config(text=f"{m['year']} | {m['genre']} | Rating: {m['rating']}")
            desc_lbl.config(text=m["description"])

    listbox.bind("<<ListboxSelect>>", show_movie)

    # ------------------ ADMIN PANEL ------------------

    def movie_form(edit=False):
        win = tk.Toplevel(app)
        win.title("Edit Movie" if edit else "Add Movie")
        entries = {}

        fields = ["Title", "Year", "Genre", "Rating", "Description"]
        for i, field in enumerate(fields):
            tk.Label(win, text=field).grid(row=i, column=0)
            e = tk.Entry(win, width=40)
            e.grid(row=i, column=1)
            entries[field.lower()] = e

        if edit and listbox.curselection():
            m = movies[listbox.curselection()[0]]
            entries["title"].insert(0, m["title"])
            entries["year"].insert(0, m["year"])
            entries["genre"].insert(0, m["genre"])
            entries["rating"].insert(0, m["rating"])
            entries["description"].insert(0, m["description"])

        def save():
            data = {k: v.get() for k, v in entries.items()}
            if edit:
                movies[listbox.curselection()[0]] = data
            else:
                movies.append(data)
            save_movies()
            refresh_list()
            win.destroy()

        tk.Button(win, text="Save", command=save).grid(row=6, columnspan=2, pady=10)

    def delete_movie():
        if listbox.curselection():
            del movies[listbox.curselection()[0]]
            save_movies()
            refresh_list()

    # ------------------ LOGOUT ------------------

    def logout():
        app.destroy()
        open_login()

    # ------------------ ADMIN BUTTONS ------------------

    if current_role == "admin":
        admin_frame = tk.Frame(left)
        admin_frame.pack(pady=10)

        tk.Button(admin_frame, text="➕ Add", command=lambda: movie_form()).pack(fill="x")
        tk.Button(admin_frame, text="✏️ Edit", command=lambda: movie_form(edit=True)).pack(fill="x")
        tk.Button(admin_frame, text="❌ Delete", command=delete_movie).pack(fill="x")

    # ------------------ LOGOUT BUTTON ------------------

    tk.Button(left, text="🔄 Logout", command=logout).pack(pady=20, fill="x")

    app.mainloop()

# ------------------ START APP ------------------

open_login()
