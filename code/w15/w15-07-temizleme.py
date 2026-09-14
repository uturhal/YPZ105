# w15-07-temizleme.py — kirli veri: boş satırları ve hatalı sayıları atla

values = []
blank = 0
bad = 0

with open("kirli_veri.txt", encoding="utf-8") as f:
    for number, line in enumerate(f, start=1):
        text = line.strip()
        if text == "":               # boş satır
            blank += 1
            continue
        try:
            values.append(float(text))
        except ValueError:           # sayıya çevrilemeyen satır
            bad += 1
            print(f"  {number}. satır atlandı: {repr(text)}")

print(f"Geçerli: {len(values)}, boş: {blank}, hatalı: {bad}")
print(f"Ortalama sıcaklık: {sum(values) / len(values):.2f} °C")
print(f"En düşük: {min(values)}, en yüksek: {max(values)}")
