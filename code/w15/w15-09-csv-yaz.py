# w15-09-csv-yaz.py — DictReader ile okuma, writer ile yeni bir CSV yazma
import csv

MIDTERM_WEIGHT = 0.4
FINAL_WEIGHT = 0.6

rows = []
with open("ogrenciler.csv", encoding="utf-8", newline="") as f:
    for record in csv.DictReader(f):     # her satır bir sözlük
        average = (float(record["vize"]) * MIDTERM_WEIGHT
                   + float(record["final"]) * FINAL_WEIGHT)
        status = "Geçti" if average >= 60 else "Kaldı"
        rows.append([record["no"], record["ad"], f"{average:.1f}", status])

with open("sonuclar.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow(["no", "ad", "ortalama", "durum"])   # başlık satırı
    writer.writerows(rows)

# Yazılan dosyayı geri okuyup gösterelim
with open("sonuclar.csv", encoding="utf-8") as f:
    print(f.read(), end="")
