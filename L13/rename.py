import os

# Specifica calea catre folder
folder_path = "cale/catre/folderul_tau"

# Parcurge toate fisierele din folder
for filename in os.listdir(folder_path):
    old_path = os.path.join(folder_path, filename)

    # Verifica daca este fisier (nu folder)
    if os.path.isfile(old_path):
        new_filename = "renamed_" + filename
        new_path = os.path.join(folder_path, new_filename)

        os.rename(old_path, new_path)
        print(f"{filename} a fost redenumit in {new_filename}")
