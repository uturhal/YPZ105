# w08-09-ebob.py — Öklid algoritması: kalan sıfır olana kadar böl

a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))
first, second = a, b           # sonucu yazdırmak için sakla

steps = 0
while b != 0:
    remainder = a % b
    print(f"  {a} = {a // b} x {b} + {remainder}")
    a, b = b, remainder        # bölen bölünen olur, kalan bölen olur
    steps += 1

print(f"EBOB({first}, {second}) = {a}   ({steps} adım)")
