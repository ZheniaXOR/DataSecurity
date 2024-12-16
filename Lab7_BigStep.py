from math import ceil, sqrt


#Бінарне експоненціювання, заміня (base**exp) % mod
def power_mod(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def baby_step_giant_step(g, h, q):
    m = ceil(sqrt(q - 1))
    Table = {}
    for j in range(m):
        value = power_mod(g, j, q)
        Table[value] = j
    g_inv_m = power_mod(g, -m % (q - 1), q)
    y = h
    for i in range(m):
        if y in Table:
            return i * m + Table[y]
        y = (y * g_inv_m) % q
    return -1


# h = (q^x) % q
g, h, q = 49999999961, 42, 49999999967
x = baby_step_giant_step(g, h, q)
print(f"rez: x = {x}")
