def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return gcd(b, a%b)
    else:
        return gcd(a, b%a)

a, b = map(int, input().split())
print(gcd(a, b))
