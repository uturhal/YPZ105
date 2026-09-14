# w04-06-operatorler.py — Aritmetik operatörler ve işlem önceliği

print("7 + 2  =", 7 + 2)
print("7 - 2  =", 7 - 2)
print("7 * 2  =", 7 * 2)
print("7 / 2  =", 7 / 2)      # bölme: sonuç HER ZAMAN float
print("7 // 2 =", 7 // 2)     # tam bölme: aşağıya yuvarlanmış tam sayı
print("7 % 2  =", 7 % 2)      # kalan (mod)
print("7 ** 2 =", 7 ** 2)     # üs alma

print("-7 // 2 =", -7 // 2)   # aşağıya (daha küçük sayıya) yuvarlar: -4
print("-7 % 2  =", -7 % 2)    # kalan işareti bölenle aynıdır: 1
print("6 / 3   =", 6 / 3)     # tam bölünse bile float: 2.0

# İşlem önceliği: ** > (* / // %) > (+ -), aynı seviyede soldan sağa
print("2 + 3 * 4 ** 2   =", 2 + 3 * 4 ** 2)     # 2 + 3*16 = 50
print("(2 + 3) * 4 ** 2 =", (2 + 3) * 4 ** 2)   # 5*16 = 80
print("2 ** 3 ** 2       =", 2 ** 3 ** 2)       # üs alma SAĞDAN sola: 2**9 = 512
print("100 / 10 / 2      =", 100 / 10 / 2)      # soldan sağa: 5.0

# Kısaltılmış atamalar
total = 10
total += 5      # total = total + 5
total *= 2      # total = total * 2
print("total =", total)

# math modülü
import math
print("karekök(2)  =", math.sqrt(2))
print("pi          =", math.pi)
print("tavan(3.2)  =", math.ceil(3.2), " taban(3.8) =", math.floor(3.8))
print("round(2.5)  =", round(2.5), " round(3.5) =", round(3.5))   # bankacı yuvarlaması
print("round(3.14159, 2) =", round(3.14159, 2))
