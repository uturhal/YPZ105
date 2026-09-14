# w04-08-bmi.py — Vücut kitle indeksi (VKİ): girdi al, hesapla, biçimli yazdır
# VKİ = kütle (kg) / boy (m) ** 2

weight = float(input("Kütleniz (kg): "))
height = float(input("Boyunuz (m): "))

bmi = weight / height ** 2

print(f"Kütle : {weight:.1f} kg")
print(f"Boy   : {height:.2f} m")
print(f"VKİ   : {bmi:.2f}")
