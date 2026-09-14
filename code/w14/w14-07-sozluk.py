# w14-07-sozluk.py — sözlük: anahtar-değer çiftleri, ekle/sil/ara/döngü

plates = {"Trabzon": 61, "Rize": 53, "Ankara": 6}
print(plates, len(plates), plates["Trabzon"])

plates["Giresun"] = 28          # anahtar yoksa ekler
plates["Rize"] = 53             # varsa günceller
print(plates)

print("Rize" in plates, "Artvin" in plates, 61 in plates)   # in: ANAHTAR
print(plates.get("Artvin"), plates.get("Artvin", "kayıt yok"))

del plates["Rize"]
code = plates.pop("Giresun")    # pop silinen değeri döndürür
print("Silinen Giresun kodu:", code, "->", plates)

for city in plates:             # döngü yalnız anahtarları verir
    print(city, end=" ")
print()
for city, code in plates.items():          # (anahtar, değer) çiftleri
    print(f"{city:<8} {code:>3}")
print("Kodlar:", list(plates.values()))

coords = {(41.0, 39.7): "Trabzon"}         # anahtar demet de olabilir
print(coords[(41.0, 39.7)])
