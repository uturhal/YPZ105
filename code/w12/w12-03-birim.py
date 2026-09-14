# w12-03-birim.py — Yardımcı fonksiyonlar ve main(): birim dönüştürücü

KM_PER_MILE = 1.609344


def km_to_mile(km):
    return km / KM_PER_MILE


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def read_positive(prompt):
    """Geçerli (pozitif) bir sayı girilene kadar sorar."""
    while True:
        text = input(prompt)
        if text.replace(".", "", 1).isdigit() and float(text) > 0:
            return float(text)
        print("Lütfen pozitif bir sayı girin.")


def convert(choice, value):
    """Uygun yardımcıyı çağırır; sonucu VE birimini döndürür."""
    if choice == 1:
        return km_to_mile(value), "mil"
    return celsius_to_fahrenheit(value), "°F"


def main():
    print("1) km -> mil     2) °C -> °F")
    choice = int(input("Seçiminiz (1-2): "))
    value = read_positive("Değer: ")
    result, unit = convert(choice, value)     # iki değer birden
    print(f"Sonuç: {result:.2f} {unit}")


main()
