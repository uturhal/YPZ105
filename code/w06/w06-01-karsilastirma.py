# w06-01-karsilastirma.py — bool, karşılaştırma operatörleri, zincirleme

score = 72
print(score > 50, score == 72, score != 72)   # True True False
print(type(score > 50))                       # <class 'bool'>

# Karşılaştırmanın sonucu bir değişkende saklanabilir
passed = score >= 60
print("Geçti mi?", passed)

# int ile float değerce karşılaştırılır; metin ile sayı asla eşit olmaz
print(5 == 5.0, "5" == 5)            # True False

# Metinler karakter karakter, Unicode sırasına göre karşılaştırılır
print("elma" < "erik")               # True: 'l' < 'r'
print("Zeynep" < "ali")              # True: büyük harfler önce gelir

# Zincirleme karşılaştırma: matematikteki gibi yazılır
x = 7
print(0 <= x < 10, 0 <= x < 5)       # True False
