def multiples(n):
    return [ n * i for i in range(1, 10) ]

def counts(n):
    l = multiples(n)
    s = "".join(str(i) for i in l)
    return [ s.count(str(j)) for j in range(10) ]

def is_microwave(n):
    c = counts(n)
    return min(c) >= max(c) - 1

def simple_is_microwave(n):
    l = [ n * i for i in range(1, 11) ]
    s = "".join(str(i) for i in l)
    c = [ s.count(str(j)) for j in range(10) ]
    return min(c) >= max(c) - 1
