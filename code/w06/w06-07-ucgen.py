# w06-07-ucgen.py — üçgen eşitsizliği ve üçgen türü

a = float(input("1. kenar: "))
b = float(input("2. kenar: "))
c = float(input("3. kenar: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Kenar uzunlukları pozitif olmalıdır.")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Bu üç kenarla üçgen oluşmaz.")
elif a == b == c:
    print("Eşkenar üçgen.")
elif a == b or a == c or b == c:
    print("İkizkenar üçgen.")
else:
    print("Çeşitkenar üçgen.")
