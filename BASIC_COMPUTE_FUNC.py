
def Relatively_Prime(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def Gcd(a, m):
    if Relatively_Prime(a, m) != 1 and Relatively_Prime(a, m) != -1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    if u1 > 0:
        return u1 % m
    else:
        return (u1 + m) % m

# InECC
def Add(m, n):
    if (m == 0):
        return n
    if (n == 0):
        return m
    he = []
    if (m != n):
        if (Relatively_Prime(m[0] - n[0], p) != 1 and Relatively_Prime(m[0] - n[0], p) != -1):
            return 0
        else:
            k = ((m[1] - n[1]) * Gcd(m[0] - n[0], p)) % p
    else:
        k = ((3 * (m[0] ** 2) + a) * Gcd(2 * m[1], p)) % p
    x = (k ** 2 - m[0] - n[0]) % p
    y = (k * (m[0] - x) - m[1]) % p
    he.append(x)
    he.append(y)
    return he

def Multiply(n, l):
    if n == 0:
        return 0
    if n == 1:
        return l
    t = l
    while (n >= 2):
        t = Add(t, l)
        n = n - 1
    return t
