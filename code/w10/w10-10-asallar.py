# w10-10-asallar.py — for … else ile asal testi ve 2–100 arası asallar

n = int(input("Bir sayı: "))

if n < 2:
    print(n, "asal değil (2'den küçük)")
else:
    for divisor in range(2, n):              # bir bölen ara
        if n % divisor == 0:
            print(f"{n} asal değil: {divisor} ile bölünür")
            break
    else:                                    # break OLMADAN bitti
        print(n, "asal")

print("2–100 arası asallar:")                # aynı desen, iç döngü olarak
count = 0
for candidate in range(2, 101):
    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            break
    else:
        print(candidate, end=" ")
        count += 1
print("\nToplam:", count, "asal")
