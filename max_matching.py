from math import factorial


def maximum_matching(seq):

    a = seq.count('A')
    u = seq.count('U')
    c = seq.count('C')
    g = seq.count('G')

    if a > u:
        maximum_matching_au = factorial(a) / factorial(a - u)
    else:
        maximum_matching_au = factorial(u) / factorial(u - a)
    if c > g:
        maximum_matching_gc = factorial(c) / factorial(c - g)
    else:
        maximum_matching_gc = factorial(g) / factorial(g - c)

    return int(maximum_matching_au * maximum_matching_gc)


rna = "AUGCUUC"
print(maximum_matching(rna))
