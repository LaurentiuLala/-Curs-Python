def unique_pair_sum(numbers, target):
    try:
        # Verificam tipul inputului
        if not isinstance(numbers, list):
            raise TypeError("numbers trebuie sa fie o lista de numere.")
        if not isinstance(target, (int, float)):
            raise TypeError("target trebuie sa fie un numar.")

        seen = set()
        pairs = set()

        for num in numbers:
            if not isinstance(num, (int, float)):
                raise TypeError("Toate elementele din numbers trebuie sa fie numere.")

            complement = target - num

            if complement in seen:
                pair = tuple(sorted((num, complement)))
                pairs.add(pair)

            seen.add(num)

        return pairs

    except TypeError as e:
        print(f"Eroare de tip: {e}")
        return set()
    except Exception as e:
        print(f"Eroare neasteptata: {e}")
        return set()


numbers = [1, 2, 3, 4, 3, 5, 6]
target = 7
print(unique_pair_sum(numbers, target))
