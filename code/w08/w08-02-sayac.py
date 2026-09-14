# w08-02-sayac.py — sayaç kontrollü döngüler: ileri, ikişer, geri

n = int(input("Bir sayı girin: "))

# 1'den n'e kadar tüm sayılar, aynı satırda
i = 1
while i <= n:
    print(i, end=" ")
    i += 1
print()                        # satırı bitir

# 2'den n'e kadar çift sayılar: sayaç ikişer artar
i = 2
while i <= n:
    print(i, end=" ")
    i += 2
print()

# n'den 1'e geri sayım: sayaç azalır, koşul ters döner
i = n
while i >= 1:
    print(i, end=" ")
    i -= 1
print("Kalkış!")
