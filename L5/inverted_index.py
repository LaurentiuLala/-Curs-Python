def inverted_index(documents):
    index = {}

    for doc_index, document in enumerate(documents):
        words = document.lower().split()

        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(doc_index)

    return index


documents = [
    "pisica a stat pe covor",
    "cainele a stat în ceață",
    "pisica și câinele s-au jucat împreună"
]

result = inverted_index(documents)
print(result)
