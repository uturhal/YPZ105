# w06-10-vki-sinifi.py — VKİ hesabı + dört dallı sınıflandırma

weight = float(input("Kütleniz (kg): "))
height = float(input("Boyunuz (m): "))

bmi = weight / height ** 2

if bmi < 18.5:
    category = "zayıf"
elif 18.5 <= bmi < 25:
    category = "normal"
elif 25 <= bmi < 30:
    category = "fazla kilolu"
else:
    category = "obez"

print(f"VKİ: {bmi:.2f} -> {category}")
