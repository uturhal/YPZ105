# w07-06-dogrulama.py — Girdi doğrulama: isdigit(), try/except, aralık

# 1) Tam sayı bekliyoruz: isdigit() ile biçim kontrolü
age_text = input("Yaşınız: ")
if age_text.isdigit():
    age = int(age_text)
    if 0 < age < 120:
        print(f"Yaş kabul edildi: {age}")
    else:
        print("Yaş 1 ile 119 arasında olmalı.")
else:
    print(f"'{age_text}' bir tam sayı değil.")

# 2) Ondalıklı sayı bekliyoruz: isdigit() yetmez ("1.75" için False verir)
height_text = input("Boyunuz (m): ")
try:
    height = float(height_text)       # başarısız olursa ValueError fırlar
    is_number = True
except ValueError:
    is_number = False

if not is_number:
    print(f"'{height_text}' sayı değil; ondalık ayırıcı NOKTA olmalı: 1.75")
elif not 0.5 <= height <= 2.5:
    print("Boy 0.5 ile 2.5 m arasında olmalı.")
else:
    print(f"Boy kabul edildi: {height:.2f} m")
