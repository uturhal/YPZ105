# w04-07-fstring.py — print ayarları ve f-string ile biçimli çıktı

name = "Mehmet"
score = 87.4567
count = 1234567

# print: sep ayırıcıyı, end satır sonunu değiştirir
print("a", "b", "c")
print("a", "b", "c", sep="-")
print("Satır sonu yok", end=" | ")
print("aynı satırda devam")

# f-string: metnin içine {} ile değer gömme
print(f"Öğrenci {name}, puan {score}")
print(f"Puan (2 ondalık): {score:.2f}")
print(f"Puan (yüzde işareti gibi): {score / 100:.1%}")
print(f"Binlik ayırıcı: {count:,}")
print(f"Sağa dayalı 10 karakter: [{name:>10}]")
print(f"Sola dayalı 10 karakter: [{name:<10}]")
print(f"Ortalanmış 10 karakter : [{name:^10}]")
print(f"Sıfırla doldur: {42:05d}")
print(f"İfade de yazılabilir: {3 * 7 = }")

# Kaçış karakterleri
print("Tab\tile ayrılmış\tsütunlar")
print("Alt satıra\ngeçmek için \\n kullanılır")
print("Tırnak içinde \"tırnak\" yazmak")
print('Tek tırnaklı metinde "çift tırnak" serbesttir')
