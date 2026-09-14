# w10-03-sesli-harf.py — Metin üzerinde for: sesli harf, büyük harf, rakam

VOWELS = "aeıioöuüAEIİOÖUÜ"
text = input("Bir cümle yazın: ")

vowel_count = 0                      # sayaçlar döngüden ÖNCE sıfırlanır
upper_count = 0
digit_count = 0
for ch in text:                      # ch: sırayla metnin her karakteri
    if ch in VOWELS:
        vowel_count += 1
    if ch.isupper():
        upper_count += 1
    if ch.isdigit():
        digit_count += 1

print(f"Karakter sayısı : {len(text)}")
print(f"Sesli harf      : {vowel_count}")
print(f"Büyük harf      : {upper_count}")
print(f"Rakam           : {digit_count}")
