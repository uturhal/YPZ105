# w13-04-dongu-girdi.py — Listeyi girdiyle doldurma ve üç döngü biçimi

scores = []
while True:                        # nöbetçi değer: -1 girilince dur
    value = int(input("Not (-1 = bitir): "))
    if value == -1:
        break
    scores.append(value)

for piece in input("Kalan notlar: ").split():   # split parçalara ayırır
    scores.append(int(piece))
print("Liste:", scores, "| eleman:", len(scores))

total = 0                          # 1) yalnız DEĞER gerekiyorsa
for s in scores:
    total += s
print(f"Ortalama: {total / len(scores):.1f}")

for i, s in enumerate(scores, start=1):   # 2) SIRA NUMARASI gerekiyorsa
    print(f"  {i}. öğrenci: {s}")

for i in range(len(scores)):       # 3) elemanı DEĞİŞTİRMEK gerekiyorsa
    scores[i] = min(scores[i] + 5, 100)
print("Güncel:", scores)
