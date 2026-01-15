def reverse_lines(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:

            for line in infile:
                outfile.write(line.rstrip()[::-1] + '\n')

    except FileNotFoundError:
        print(f"Eroare: Fișierul '{input_file}' nu a fost găsit.")
    except IOError:
        print("Eroare la citirea sau scrierea fișierelor.")
    except Exception as e:
        print(f"Eroare neașteptată: {e}")
