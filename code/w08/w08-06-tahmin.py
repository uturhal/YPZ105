# w08-06-tahmin.py — sayı tahmin oyunu: while True, break ve continue

import random

secret = random.randint(1, 100)        # 1-100 arası rastgele sayı
attempts = 0
print("1 ile 100 arasında bir sayı tuttum. Bil bakalım!")

while True:                            # çıkış yalnız break ile
    guess = int(input("Tahminin: "))
    if guess < 1 or guess > 100:
        print("  Aralık dışı, bu deneme sayılmaz.")
        continue                       # kalanı atla, koşula dön
    attempts += 1
    if guess < secret:
        print("  Daha büyük.")
    elif guess > secret:
        print("  Daha küçük.")
    else:
        print(f"Doğru! {attempts} denemede buldun.")
        break                          # döngüden çık
