# w10-02-for-vs-while.py — Aynı problem iki döngüyle: 1'den n'e toplam

n = int(input("n: "))

total_w = 0                          # while: sayaç, koşul, artış ayrı
i = 1
while i <= n:
    total_w += i
    i += 1

total_f = 0                          # for: üçü de range'in içinde
for i in range(1, n + 1):
    total_f += i

print(f"while ile              : {total_w}")
print(f"for ile                : {total_f}")
print(f"Gauss formülü n(n+1)/2 : {n * (n + 1) // 2}")
