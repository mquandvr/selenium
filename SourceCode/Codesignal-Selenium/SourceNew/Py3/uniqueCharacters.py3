def uniqueCharacters(document):
    return sorted([char for index, char in enumerate(document) if char not in document[0:index]])
