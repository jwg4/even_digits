def multiples(n):
    return [ n * i for i in range(1, 10) ]

def counts(n):
    l = multiples(n)
    s = "".join(str(i) for i in l)
    return [ s.count(str(j)) for j in range(10) ]
