def differentSubstringsTrie(inp):
    s = set()
    for i in range(len(inp)):
        for j in range(i+1, len(inp)+1):
            s.add(inp[i:j])
    print(s)
    return len(s)
            