# w08-08-collatz.py — Collatz dizisi: 1'e ulaşmak kaç adım sürer?

n = int(input("Başlangıç sayısı: "))
steps = 0
peak = n                       # dizide görülen en büyük değer

while n != 1:
    if n % 2 == 0:
        n = n // 2             # çiftse yarıya
    else:
        n = 3 * n + 1          # tekse üç katının bir fazlası
    steps += 1
    if n > peak:
        peak = n

print(f"Adım sayısı: {steps}")
print(f"En büyük değer: {peak}")
