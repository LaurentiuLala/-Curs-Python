def inverted_index(documents):
    try:
        # Verificam daca inputul este o lista
        if not isinstance(documents, list):
            raise TypeError("Inputul trebuie sa fie o lista de stringuri.")

        index = {}

        for doc_index, document in enumerate(documents):
            # Verificam daca fiecare document este string
            if not isinstance(document, str):
                raise TypeError("Fiecare document trebuie sa fie un string.")

            words = document.lower().split()

            for word in words:
                if word not in index:
                    index[word] = set()
                index[word].add(doc_index)

        return index

    except TypeError as e:
        print(f"Eroare de tip: {e}")
        return {}
    except Exception as e:
        print(f"Eroare neasteptata: {e}")
        return {}


documents = [
    "pisica a stat pe covor",
    "cainele a stat în ceață",
    "pisica și câinele s-au jucat împreună"
]

result = inverted_index(documents)
print(result)
