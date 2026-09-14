# w13-11-not-istatistik.py — Not listesi: istatistikler ve frekans
import statistics

scores = [72, 85, 91, 58, 77, 85, 64, 96]
n = len(scores)
mean = sum(scores) / n

ordered = sorted(scores)          # medyan: sıralı listenin ortası
if n % 2 == 1:
    median = ordered[n // 2]
else:
    median = (ordered[n // 2 - 1] + ordered[n // 2]) / 2

mode = scores[0]                  # mod: en çok tekrar eden değer
for s in scores:
    if scores.count(s) > scores.count(mode):
        mode = s

print(f"{'':10}{'elle':>8}{'statistics':>12}")
print(f"{'Ortalama':10}{mean:>8.2f}{statistics.mean(scores):>12.2f}")
print(f"{'Medyan':10}{median:>8.2f}{statistics.median(scores):>12.2f}")
print(f"{'Mod':10}{mode:>8}{statistics.mode(scores):>12}")
above = [s for s in scores if s > mean]
print(f"Ortalama üstü: {above} ({len(above)} öğrenci)")

labels = ["A", "B", "C", "D", "F"]   # frekans: sayaç listesi (sözlük yok)
limits = [90, 80, 70, 60, 0]
counts = [0] * 5
for s in scores:
    for k in range(5):
        if s >= limits[k]:
            counts[k] += 1
            break
for k in range(5):
    print(f"  {labels[k]} {'*' * counts[k]:<6}{counts[k]}")
print("Toplam:", sum(counts))
