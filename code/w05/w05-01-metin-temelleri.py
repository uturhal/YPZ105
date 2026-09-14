# w05-01-metin-temelleri.py — Tırnaklar, çok satırlı metin, kaçış
# karakterleri, ham metin; len(), + ve * operatörleri, in / not in

city = "Trabzon"                    # çift tırnak
course = 'Programlama'              # tek tırnak: aynı şey
quote = "Ali 'geldi' dedi"       # tek tırnak varsa çift ile aç
print(city, course, "|", quote)

# Çok satırlı metin: üç tırnak arasındaki satır sonları korunur
address = """Trabzon Üniversitesi
Yapay Zeka Mühendisliği"""
print(address)

# Kaçış karakterleri (\t sekme, \n yeni satır) ve ham metin
print("Ad\tSoyad\nAli\tKaya")
print("C:\\Users\\ayse", r"C:\Users\ayse")   # aynı sonuç

# len(): karakter sayısı (boşluk ve noktalama dahil)
sentence = "Yapay zeka mühendisliği"
print("Karakter sayısı:", len(sentence), "| boş metin:", len(""))

# + birleştirir, * yineler
full_name = "Ayşe" + " " + "Yılmaz"
print(full_name, len(full_name), "-" * 12)

# in / not in: alt metin var mı? Sonuç True ya da False
print("zeka" in sentence, "Zeka" in sentence, "x" not in sentence)
