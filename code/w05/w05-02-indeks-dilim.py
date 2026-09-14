# w05-02-indeks-dilim.py — İndeksleme, dilimleme, ters çevirme

word = "Merhaba"
print(word[0], word[1], word[6])     # pozitif indeks: 0'dan
print(word[-1], word[-2], word[-7])  # negatif indeks: -1'den

# Dilimleme: word[a:b] → a dahil, b hariç
print(word[0:3], word[3:7])             # Mer haba
print(word[:3], word[3:])               # baştan / sona kadar
print(word[-4:], word[:-1])             # son dört / sonuncu hariç
print(word[::2], word[1::2], word[::-1])   # adımlı ve ters dilim

# Sınır dışı DİLİM hata vermez; kısa ya da boş metin döner
print(word[3:100], "[" + word[10:20] + "]")

# Uygulama: son dört hane dışında maskeleme
phone = "05321234567"
print("Telefon:", "*" * (len(phone) - 4) + phone[-4:])
id_no = "12345678901"
print("Kimlik :", id_no[:2] + "*" * 7 + id_no[-2:])
