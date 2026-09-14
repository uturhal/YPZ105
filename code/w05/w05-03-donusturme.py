# w05-03-donusturme.py — Harf büyüklüğü ve kenar boşluğu metotları,
# metot zincirleme

text = "programlama DERS notu"
print(text.upper())         # hepsi büyük
print(text.lower())         # hepsi küçük
print(text.title())         # her sözcüğün ilk harfi büyük
print(text.capitalize())    # yalnız ilk harf büyük, gerisi küçük
print(text.swapcase())      # büyük -> küçük, küçük -> büyük
print(text)                 # metot metni DEĞİŞTİRMEZ: hâlâ orijinal

# Değişikliği saklamak için sonucu bir ada atayın
text = text.title()
print(text)

# strip / lstrip / rstrip: kenarlardaki boşlukları (ve \n) atar
raw = "   ayşe kaya   "
print("[" + raw.strip() + "]", "[" + raw.rstrip() + "]")

# Argüman verilirse o karakterleri kenarlardan atar
print("***Dikkat***".strip("*"), "www.trabzon.edu.tr".lstrip("w."))

# Metot zincirleme: her metot bir öncekinin sonucuna uygulanır
print("   aYŞE kAYA  ".strip().lower().title())
