def filter_lines(input_file, output_file, keyword):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:

            for line in infile:
                if keyword in line:
                    outfile.write(line)

    except FileNotFoundError:
        print(f"Eroare: Fișierul '{input_file}' nu a fost găsit.")
    except IOError:
        print("Eroare la citirea sau scrierea fișierelor.")
    except Exception as e:
        print(f"Eroare neașteptată: {e}")
