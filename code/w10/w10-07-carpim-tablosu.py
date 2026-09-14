# w10-07-carpim-tablosu.py — İç içe for ile hizalı çarpım tablosu (1–9)

N = 9

print("    |", end="")                       # başlık: sütun numaraları
for j in range(1, N + 1):
    print(f"{j:>4}", end="")
print()
print("----+" + "----" * N)

for i in range(1, N + 1):                    # dış döngü: satırlar
    print(f"{i:>3} |", end="")
    for j in range(1, N + 1):                # iç döngü: sütunlar
        print(f"{i * j:>4}", end="")
    print()                                  # iç döngü bitti: satır sonu
