# w08-01-ilk-dongu.py — ilk while döngüsü: 1'den 5'e kadar yazdırma

i = 1                          # (1) başlangıç: sayaç ilk değerini alır
while i <= 5:                  # (2) koşul: doğruysa gövde yine çalışır
    print("Tur:", i)           # (3) gövde: girintili satırlar
    i = i + 1                  # (4) güncelleme: sayaç bir ilerler
print("Döngü bitti. i =", i)   # koşul yanlışlanınca buraya gelinir
