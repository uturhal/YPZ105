# w11-10-sayi-fonksiyonlari.py — 8. ve 10. haftanın döngüleri fonksiyon oldu

def factorial(n):
    """n! = 1 * 2 * ... * n  (0! = 1)"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(a, b):
    """En büyük ortak bölen (Öklid algoritması)."""
    while b != 0:
        a, b = b, a % b
    return a


def digit_sum(n):
    """Pozitif tam sayının basamakları toplamı."""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10                # n yerel bir addır: dışarıyı etkilemez
    return total


print("5! =", factorial(5), " 10! =", factorial(10))
print("gcd(48, 18) =", gcd(48, 18), " gcd(17, 5) =", gcd(17, 5))
number = 2026
print("digit_sum(2026) =", digit_sum(number), " number hâlâ", number)
# Dönüş değerleri başka ifadelerde birleştirilebilir
print("digit_sum(9875) =", digit_sum(9875),
      " EKOK(12, 18) =", 12 * 18 // gcd(12, 18))
