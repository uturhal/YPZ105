# w10-04-sezar.py — Sezar şifresi: harfleri k adım kaydır (ord/chr, mod 26)

message = input("Mesaj (İngiliz alfabesi, BÜYÜK harf): ")
shift = int(input("Kayma miktarı: "))

encrypted = ""
for ch in message:
    if "A" <= ch <= "Z":                     # yalnız harfler kaydırılır
        position = ord(ch) - ord("A")        # A→0, B→1, ..., Z→25
        encrypted += chr((position + shift) % 26 + ord("A"))
    else:
        encrypted += ch                      # boşluk, rakam aynı kalır

decrypted = ""                               # çözme: ters yönde kayma
for ch in encrypted:
    if "A" <= ch <= "Z":
        decrypted += chr((ord(ch) - ord("A") - shift) % 26 + ord("A"))
    else:
        decrypted += ch

print("Şifreli mesaj:", encrypted)
print("Geri çözüm   :", decrypted)
print("Kontrol      :", decrypted == message)
