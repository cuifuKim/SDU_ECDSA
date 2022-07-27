def Ecdsa_Sign(m, n, G, d,k):
    e = hash(m)
    R = Multiply(k, G)
    r = R[0] % n
    s = (Gcd(k, n) * (e + d * r)) % n
    return r, s

def Ecdsa_Verify(m, n, G, r, s, P):
    e = hash(m)
    w = Gcd(s, n)
    v1 = (e * w) % n
    v2 = (r * w) % n
    w = Add(Multiply(v1, G), Multiply(v2, P))
    if (w == 0):
        print('false')
        return False
    else:
        if (w[0] % n == r):
            print('true')
            return True
        else:
            print('false')
            return False
