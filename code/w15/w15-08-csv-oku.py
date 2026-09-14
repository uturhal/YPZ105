# w15-08-csv-oku.py — CSV'yi elle (split) ve csv modülüyle okuma; istatistik
import csv

# 1) Elle: her satırı virgülden böl
with open("ogrenciler.csv", encoding="utf-8") as f:
    header = f.readline().strip().split(",")
    print("Sütunlar:", header)
    for number, line in enumerate(f):    # başlıktan sonraki satırlar
        if number < 2:                   # ilk iki kayıt yeter
            print(line.strip().split(","))

# 2) csv modülü: bölme işini o yapar; alanlar yine METİN gelir
midterms = []
finals = []
best_name = ""
best_final = 0.0
with open("ogrenciler.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    next(reader)                     # başlık satırını atla
    for row in reader:
        no, name, midterm, final = row
        midterms.append(float(midterm))
        finals.append(float(final))
        if float(final) > best_final:
            best_final = float(final)
            best_name = name

print(f"Vize ortalaması : {sum(midterms) / len(midterms):.2f}")
print(f"Final ortalaması: {sum(finals) / len(finals):.2f}")
print(f"En yüksek final : {best_name} ({best_final:.0f})")
