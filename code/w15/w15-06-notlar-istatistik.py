# w15-06-notlar-istatistik.py — notlar.txt: toplam, ortalama, en yüksek

total = 0.0
count = 0
best_name = ""
best_score = -1.0

with open("notlar.txt", encoding="utf-8") as f:
    for line in f:
        name, score_text = line.split()   # "Ayşe 85\n" -> ["Ayşe", "85"]
        score = float(score_text)         # dosyadan gelen her şey metindir
        total += score
        count += 1
        if score > best_score:
            best_score = score
            best_name = name

print(f"Öğrenci sayısı : {count}")
print(f"Toplam         : {total:.1f}")
print(f"Ortalama       : {total / count:.2f}")
print(f"En yüksek      : {best_name} ({best_score})")
