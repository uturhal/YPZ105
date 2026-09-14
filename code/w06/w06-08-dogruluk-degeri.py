# w06-08-dogruluk-degeri.py — doğruluk değeri olan nesneler ve koşullu ifade

print(bool(0), bool(0.0), bool(""), bool(None))    # hepsi False
print(bool(7), bool(-1), bool("0"), bool(" "))      # hepsi True

name = input("Adınız (boş bırakabilirsiniz): ")

if name:                        # name boş metin değilse True
    print(f"Merhaba, {name}!")
else:
    print("Merhaba, yabancı!")

# Koşullu ifade: değer seçen tek satırlık if-else
score = 58
status = "geçti" if score >= 50 else "kaldı"
print("Durum:", status)

n = -4
print("Mutlak değer:", n if n >= 0 else -n)
