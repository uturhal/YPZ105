# w11-08-asal.py — is_prime(n) fonksiyonu ve onunla 2-100 arasındaki asallar

def is_prime(n):
    """n asal ise True, değilse False döndürür."""
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False        # bölen bulundu: hemen çık
    return True                 # döngü bitti, bölen yok


print("is_prime(2) =", is_prime(2), " is_prime(91) =", is_prime(91))
print("2-100 arasındaki asallar:")
count = 0
for n in range(2, 101):
    if is_prime(n):
        print(n, end=" ")
        count += 1
print()
print("Toplam:", count)
