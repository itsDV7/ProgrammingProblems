# GCD log(ab)
def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    a = a%b
    return gcd(b, a)

# LCM log(ab)
def lcm(a, b):
    return (a * b)//gcd(a, b)
