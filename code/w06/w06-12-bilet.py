# w06-12-bilet.py — sinema bileti: yaş ve güne göre fiyat

FULL_PRICE = 180                      # TL

age = int(input("Yaş: "))
day = input("Gün (örn. Salı): ").lower()

if day == "çarşamba":                # halk günü: yarı fiyat
    price = FULL_PRICE * 0.5
elif age < 12 or age >= 65:           # çocuk ve 65 yaş üstü
    price = FULL_PRICE * 0.6
elif age <= 25:                       # genç
    price = FULL_PRICE * 0.8
else:
    price = FULL_PRICE

print(f"Bilet fiyatı: {price:.2f} TL")
