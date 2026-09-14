# w05-04-arama-sinama.py — Arama (find, rfind, index, count),
# değiştirme (replace) ve sınama (is...) metotları

sentence = "Yapay zeka, veri ile öğrenen sistemler tasarlar."

# find: ilk konum, yoksa -1 (hata vermez). rfind: son konum
print(sentence.find("zeka"), sentence.find("robot"))
print(sentence.find("e"), sentence.rfind("e"))
print(sentence.index("veri"))         # index: bulamazsa ValueError
print(sentence.count("e"), "aaaa".count("aa"))   # çakışmayan
print(sentence.startswith("Yapay"), "rapor.pdf".endswith(".pdf"))

# replace: TÜM geçişleri değiştirir, yeni metin döndürür
print(sentence.replace("e", "3", 2))  # en fazla 2 değişiklik

# Uygulama: sansürleme
comment = "Bu film berbat, oyuncular berbat, müzik berbat."
bad_word = "berbat"
print(comment.replace(bad_word, "*" * len(bad_word)))

# Sınama metotları: metnin TAMAMI koşulu sağlıyorsa True
print("2026105017".isdigit(), "3.5".isdigit(), "".isdigit())
print("Ayşe".isalpha(), "Ayşe Kaya".isalpha(), "abc123".isalnum())
print("   ".isspace(), "TRABZON".isupper(), "Trabzon".islower())
