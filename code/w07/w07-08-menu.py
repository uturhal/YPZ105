# w07-08-menu.py — Menü tabanlı program (tek seçim): birim dönüştürücü
# 8. haftada bu menü döngüye alınacak: "Çıkış" seçilene kadar yinelenecek.

print("=== Birim Dönüştürücü ===")
print("1) Kilometre -> mil")
print("2) Kilogram  -> libre")
print("3) Celsius   -> Fahrenheit")
print("4) Çıkış")
choice = input("Seçiminiz (1-4): ").strip()

match choice:
    case "1":
        km = float(input("Kilometre: "))
        print(f"{km} km = {km * 0.621371:.2f} mil")
    case "2":
        kg = float(input("Kilogram: "))
        print(f"{kg} kg = {kg * 2.20462:.2f} lb")
    case "3":
        c = float(input("Celsius: "))
        print(f"{c} °C = {c * 9 / 5 + 32:.1f} °F")
    case "4":
        print("Güle güle!")
    case _:
        print(f"Geçersiz seçim: '{choice}'. 1-4 arası bir sayı girin.")
