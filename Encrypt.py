def translate(str):
    d = {}
    for c in [65,97]:
        for i in range(26):
            d[chr(c+i)] = chr(c+(i+13)%26)
    return ''.join([d.get(c,c) for c in str])