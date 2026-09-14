# w07-07-otopark.py — Otopark ücreti: süre dilimleri ve sınır değerleri
# Tarife (kurgusal): <=30 dk 0; <=120 dk 40; <=360 dk 80; <=1440 dk 150 TL;
# 1440 dakikayı aşarsa başlayan her gün 150 TL
import math

minutes_text = input("Park süresi (dakika): ")

if not minutes_text.isdigit():
    print("Hata: süre pozitif bir tam sayı olmalı.")
else:
    minutes = int(minutes_text)
    if minutes <= 30:
        fee = 0
    elif minutes <= 120:
        fee = 40
    elif minutes <= 360:
        fee = 80
    elif minutes <= 1440:
        fee = 150
    else:
        days = math.ceil(minutes / 1440)      # başlayan gün tam gün sayılır
        fee = 150 * days
    hours, rem = divmod(minutes, 60)
    print(f"Süre: {hours} sa {rem} dk  ->  ücret: {fee} TL")
