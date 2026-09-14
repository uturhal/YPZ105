# w04-09-daire.py — Yarıçapı verilen dairenin çevresi ve alanı
import math

radius = float(input("Yarıçap (cm): "))

perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"Çevre: {perimeter:.2f} cm")
print(f"Alan : {area:.2f} cm²")
