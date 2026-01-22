def write_results_to_file(filename, results):
    with open(filename, "w", encoding="utf-8") as file:
        for key, value in results.items():
            file.write(f"{key}: {value}\n")

def read_numbers_from_file(filename):
    numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                numbers.append(int(line))
    return numbers

