# w04-04-donusum.py — input() her zaman metin döndürür; tür dönüşümü gerekir

age_text = input("Yaşınızı girin: ")
print("Girilen değer:", age_text, "-> türü:", type(age_text))

age = int(age_text)              # metinden tam sayıya
print("10 yıl sonra yaşınız:", age + 10)

height = float(input("Boyunuzu metre olarak girin: "))
print("Boyunuz santimetre olarak:", height * 100)

# Sayıdan metne dönüşüm: metinle birleştirmek için gerekir
message = "Yaş: " + str(age) + ", Boy: " + str(height) + " m"
print(message)

# Dönüşümler bilgi kaybedebilir
print(int(3.99))        # ondalık kısım ATILIR, yuvarlanmaz -> 3
print(int(-3.99))       # -> -3
print(float(7))         # -> 7.0
print(int("0042"))      # baştaki sıfırlar önemsiz -> 42
print(bool(0), bool(5), bool(""), bool("hayır"))
