# w06-05-mantiksal.py — and, or, not: doğruluk tablosu, öncelik, kısa devre

print("and:", True and True, True and False, False and False)
print("or :", True or True, True or False, False or False)
print("not:", not True, not False)

# Gerçek koşullarla
age = 20
has_id = True
print("Sinemaya girebilir mi?", age >= 18 and has_id)

temperature = 31
print("Uyarı gerekli mi?", temperature < 0 or temperature > 30)

# Öncelik: not > and > or   (parantez her zaman daha okunaklıdır)
print(True or False and False)       # True : and önce yapılır
print((True or False) and False)     # False

# Kısa devre: sol taraf sonucu belirliyorsa sağ taraf HİÇ hesaplanmaz
x = 0
print(x != 0 and 10 / x > 1)         # False -> 10 / 0 hiç denenmez
print(x == 0 or 10 / x > 1)          # True  -> yine denenmez
