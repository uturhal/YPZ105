# w06-06-artik-yil.py — artık yıl: and / or ile bileşik koşul

year = int(input("Yıl: "))

is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

if is_leap:
    print(f"{year} artık yıldır: Şubat 29 gün çeker.")
else:
    print(f"{year} artık yıl değildir: Şubat 28 gün çeker.")
