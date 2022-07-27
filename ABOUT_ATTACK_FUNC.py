def k_Leaking(r,n,k,s,m):
    r_reverse=Gcd(r,n)
    e=hash(m)
    d=r_reverse * (k*s-e)%n
    return d

def k_Reuse(r1,s1,m1,r2,s2,m2,n):
    e1=hash(m1)
    e2=hash(m2)
    d=((s1 * e2 - s2 * e1) * Gcd((s2 * r1 - s1 * r1), n)) % n
    return d

def Use_the_Same_k(s1,m1,s2,m2,r,d1,d2,n):
    e1=hash(m1)
    e2=hash(m2)
    d2_1 = ((s2 * e1 - s1 * e2 + s2 * r * d1) * Gcd(s1 * r, n)) % n
    d1_1 = ((s1 * e2 - s2 * e1 + s1 * r * d2) * Gcd(s2 * r, n)) % n
    if(d2==d2_1 and d1_1==d1):
        print("互相计算密钥成功")
        return 1
    else:
        print("互相计算密钥错误")
        return 0

def Verify_without_m(e, n, G, r, s, P):
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
            
def Pretend(r, s, n, G, P):
    u = random.randrange(1, n - 1)
    v = random.randrange(1, n - 1)
    r1 = Add(Multiply(u, G), Multiply(v, P))[0]
    e1 = (r1 * u * Gcd(v, n)) % n
    s1 = (r1 * Gcd(v, n)) % n
    Verify_without_m(e1, n, G, r1, s1, P)

def Schnorr_Sign(m, n, G, d,k):
    R = Multiply(k, G)
    e = hash(str(R[0]) + m)
    s = (k + e * d) % n
    return R, s

def Schnorr_and_ECDSA(r1, s1, R, s2, m, n):
    e1 = int(hash(m))
    e2 = int(hash(str(R[0]) + m))
    d = ((s1 * s2 - e1) * Gcd((s1 * e2 + r1), n)) % n
    return d
