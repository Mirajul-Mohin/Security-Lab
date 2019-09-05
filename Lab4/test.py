def cf_expansion(n, d):
    e = []

    # q = n // d
    # r = n % d

    q = d // n
    r = d % n

    e.append(q)

    while r != 0:
        d, n = n, r
        q = d // n
        r = d % n
        e.append(q)

    return e

print(cf_expansion(95,73))