# w05-06-unicode.py — Karakter kodları (ord/chr), karşılaştırma,
# Türkçe harf tuzağı

# Her karakterin bir Unicode kod noktası (tam sayı) vardır
print(ord("A"), ord("Z"), ord("a"), ord("z"), ord("0"), ord(" "))
print(ord("Ç"), ord("Ü"), ord("İ"), ord("ı"), ord("Ş"))
print(chr(65), chr(97), chr(231), chr(960))
print(chr(ord("K") + 1))              # bir sonraki harf: koda 1 ekle

# Karşılaştırma kod noktalarına göre, soldan sağa yapılır
print("a" < "b", "ab" < "abc", "Ali" < "Ayşe")   # l(108)<y(121)
print("Zeynep" < "ali")      # True: büyük harfler küçüklerden önce
print("Çınar" < "Zeynep")    # False! Ç (199) > Z (90)
print("10" < "9")            # True! '1' (49) < '9' (57)

# Türkçe harf tuzağı: upper/lower İngilizce kurallarıyla çalışır
print("ı".upper(), "i".upper(), "I".lower())    # I I i
print("İ".lower() == "i", len("İ".lower()))     # False 2  (!)
print("ISPARTA".lower(), "istanbul".upper())

# Çözüm: sorunlu harfleri önce elle değiştir, sonra çevir
print("ISPARTA İLİ".replace("I", "ı").replace("İ", "i").lower())
print("ısparta ili".replace("ı", "I").replace("i", "İ").upper())
