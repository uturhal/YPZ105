# w11-11-menu-once.py — Menü programı, fonksiyonsuz (düzenleme ÖNCESİ)
# Tek parça: tekrar eden bloklar, uzun gövde, zor okunur.

while True:
    print()
    print("1) VKİ hesapla")
    print("2) Harf notu")
    print("0) Çıkış")
    choice = input("Seçiminiz: ")
    if choice == "1":
        weight = float(input("Kütle (kg): "))
        while weight <= 0:                      # tekrar eden blok 1
            print("Pozitif bir değer girin.")
            weight = float(input("Kütle (kg): "))
        height = float(input("Boy (m): "))
        while height <= 0:                      # tekrar eden blok 2
            print("Pozitif bir değer girin.")
            height = float(input("Boy (m): "))
        print(f"VKİ: {weight / height ** 2:.2f}")
    elif choice == "2":
        score = float(input("Puan (0-100): "))
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        print(f"Harf notu: {grade}")
    elif choice == "0":
        print("Görüşmek üzere!")
        break
    else:
        print("Geçersiz seçim.")
