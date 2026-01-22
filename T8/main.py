import os
import statistics

from file_utils import read_numbers_from_file, write_results_to_file
from analysis import average, min_max, count_even


def main():
    input_file = "input.txt"
    output_file = "output.txt"

    if not os.path.exists(input_file):
        print("Fișierul input.txt nu există.")
        return

    numbers = read_numbers_from_file(input_file)

    avg = average(numbers)
    minimum, maximum = min_max(numbers)
    even_count = count_even(numbers)

    median = statistics.median(numbers) if numbers else 0

    results = {
        "Media": avg,
        "Minim": minimum,
        "Maxim": maximum,
        "Număr valori pare": even_count,
        "Mediană": median
    }

    write_results_to_file(output_file, results)
    print("Rezultatele au fost scrise în output.txt")


if __name__ == "__main__":
    main()
