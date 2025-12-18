def unique_pair_sum(numbers, target):
    seen = set()
    pairs = set()

    for num in numbers:
        complement = target - num

        if complement in seen:

            pair = tuple(sorted((num, complement)))
            pairs.add(pair)

        seen.add(num)

    return pairs


numbers = [1, 2, 3, 4, 3, 5, 6]
target = 7
print(unique_pair_sum(numbers, target))
