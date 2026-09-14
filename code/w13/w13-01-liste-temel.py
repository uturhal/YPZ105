# w13-01-liste-temel.py — Liste oluşturma, uzunluk, indeks, dilimleme

scores = [72, 85, 91, 58, 77]     # köşeli parantez, virgülle ayrılmış
mixed = ["Ayşe", 19, 3.85, True]  # farklı türler bir arada olabilir
numbers = list(range(1, 6))       # range'i listeye çevir
zeros = [0] * 4                   # yineleme: dört tane 0

print(scores, type(scores))
print(mixed, numbers, zeros, [])
print("Eleman sayısı:", len(scores))
print("İlk:", scores[0], "Son:", scores[-1], "Üçüncü:", scores[2])

# Dilimleme [başla:bitir:adım] — bitir hariç; sonuç YENİ bir listedir
print("İlk üç  :", scores[:3], "| son iki:", scores[-2:])
print("Atlamalı:", scores[::2], "| tersten:", scores[::-1])

# Metinle aynı işlemler: birleştirme, yineleme, üyelik
print("Birleştirme:", scores + [100, 0], "| yineleme:", [1, 2] * 3)
print("Üyelik:", 85 in scores, 60 in scores)
print("Parçalama:", scores[:2] + scores[2:] == scores)
