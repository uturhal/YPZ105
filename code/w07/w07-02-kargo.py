# w07-02-kargo.py — Karar tablosundan koda: kargo ücreti (ağırlık × bölge)
# Tablo (kurgusal, TL):  bölge  1 / 2 / 3  ->  hafif 60/90/400,
#   orta 90/150/700, ağır 150/250/1200   (hafif <= 2 kg, orta <= 10 kg)

weight = float(input("Paket ağırlığı (kg): "))
region = int(input("Bölge (1 şehir içi, 2 yurt içi, 3 yurt dışı): "))

if region < 1 or region > 3:
    print("Hata: bölge kodu 1, 2 ya da 3 olmalı.")
else:
    if weight <= 2:                    # tablo satırı: hafif
        if region == 1:
            price = 60
        elif region == 2:
            price = 90
        else:
            price = 400
    elif weight <= 10:                 # tablo satırı: orta
        if region == 1:
            price = 90
        elif region == 2:
            price = 150
        else:
            price = 700
    else:                              # tablo satırı: ağır
        if region == 1:
            price = 150
        elif region == 2:
            price = 250
        else:
            price = 1200
    print(f"{weight:.1f} kg, bölge {region}: kargo ücreti {price} TL")
