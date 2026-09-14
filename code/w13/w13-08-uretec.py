# w13-08-uretec.py — Liste üreteci: döngüden tek satıra

scores = [72, 85, 91, 58, 77, 96, 45]

squares = []                 # döngüyle: 1..5 sayılarının kareleri
for n in range(1, 6):
    squares.append(n ** 2)
print("döngüyle:", squares)

# Aynı iş liste üreteciyle: [ifade for değişken in dizi]
print("üreteçle:", [n ** 2 for n in range(1, 6)])

# Süzgeçli biçim: [ifade for değişken in dizi if koşul]
print("Geçenler:", [s for s in scores if s >= 50])

# Dönüştürme: YENİ liste üretir, scores değişmez
print("Eklenmiş:", [min(s + 5, 100) for s in scores], "| özgün:", scores)

# True = 1 olduğu için koşulu sağlayanlar sum ile sayılır
print("80 ve üstü kaç kişi:", sum([s >= 80 for s in scores]))

# Metin ile liste arasında: split ayırır, join birleştirir
print("yapay zeka mühendisliği".split())
print(" | ".join([str(s) for s in scores]))
