# w10-08-desenler.py — İç içe döngüyle yıldız desenleri: sol, sağ, piramit

n = int(input("Satır sayısı: "))

print("Sol üçgen:")
for i in range(1, n + 1):           # i. satırda i yıldız
    for j in range(i):
        print("*", end="")
    print()

print("Sağ üçgen:")
for i in range(1, n + 1):           # önce n-i boşluk, sonra i yıldız
    for j in range(n - i):
        print(" ", end="")
    print("*" * i)

print("Piramit:")
for i in range(1, n + 1):           # n-i boşluk, 2i-1 yıldız
    print(" " * (n - i) + "*" * (2 * i - 1))
