def transposeDictionary(scriptByExtension):
    return sorted([(t[1],t[0]) for t in scriptByExtension.items()])
