# w12-04-ozyineleme.py — Faktöriyel, basamak toplamı ve EBOB

def factorial(n, depth=0):
    """n! değerini özyinelemeyle hesaplar; çağrıları girintili yazar."""
    pad = "  " * depth
    print(f"{pad}factorial({n}) çağrıldı")
    if n == 0:                      # taban durumu
        print(f"{pad}taban durumu -> 1")
        return 1
    result = n * factorial(n - 1, depth + 1)
    print(f"{pad}factorial({n}) = {n} * factorial({n - 1}) = {result}")
    return result


def digit_sum(n):
    """Son basamak + kalan sayının basamak toplamı."""
    if n < 10:                      # taban durumu: tek basamaklı sayı
        return n
    return n % 10 + digit_sum(n // 10)


def gcd(a, b):
    """Öklid: EBOB(a, b) = EBOB(b, a mod b); taban EBOB(a, 0) = a."""
    if b == 0:
        return a
    return gcd(b, a % b)


print("4! =", factorial(4))
print("digit_sum(4729) =", digit_sum(4729),
      "| gcd(1071, 462) =", gcd(1071, 462),
      "| gcd(48, 18) =", gcd(48, 18))
