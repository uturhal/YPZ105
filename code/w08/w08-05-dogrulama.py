# w08-05-dogrulama.py — girdi doğrulama: geçerli olana kadar sor

valid = False
while not valid:
    text = input("0-100 arası bir not girin: ")
    try:
        grade = int(text)                  # 7. hafta: metni çevir
        if 0 <= grade <= 100:
            valid = True                   # döngü sonraki turda biter
        else:
            print("  Hata: 0 ile 100 arasında olmalı.")
    except ValueError:
        print("  Hata: sayı girmelisiniz.")

print(f"Kabul edilen not: {grade}")
