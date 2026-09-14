# w10-01-range.py — range()'in üç biçimi, negatif adım ve boş aralık

print("range(5):         ", end="")
for i in range(5):                   # 0, 1, 2, 3, 4 — 5 dahil DEĞİL
    print(i, end=" ")
print("\nrange(1, 6):      ", end="")
for i in range(1, 6):                # 1'den başla, 6'dan ÖNCE dur
    print(i, end=" ")
print("\nrange(0, 20, 5):  ", end="")
for i in range(0, 20, 5):            # 5'er adımla: 0, 5, 10, 15
    print(i, end=" ")
print("\nrange(10, 0, -2): ", end="")
for i in range(10, 0, -2):           # negatif adım: geri sayım
    print(i, end=" ")
print("\nrange(5, 5):      ", end="")
for i in range(5, 5):                # boş aralık: gövde hiç çalışmaz
    print(i, end=" ")
print("(gövde hiç çalışmadı)")

for _ in range(3):                   # sayaç gerekmiyorsa adı _ olur
    print("Python!", end=" ")
print()
