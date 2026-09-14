# w11-12-menu-sonra.py — Aynı menü programı, fonksiyonlara ayrılmış (SONRA)
# Her fonksiyon tek bir iş yapar; main() yalnız akışı yönetir.

def show_menu():
    """Menü seçeneklerini yazar."""
    print()
    print("1) VKİ hesapla")
    print("2) Harf notu")
    print("0) Çıkış")


def read_positive(prompt):
    """Pozitif bir sayı okur; geçerli olana kadar yeniden sorar."""
    value = float(input(prompt))
    while value <= 0:
        print("Pozitif bir değer girin.")
        value = float(input(prompt))
    return value


def bmi(weight, height):
    """Vücut kitle indeksi: kütle (kg) / boy (m) karesi."""
    return weight / height ** 2


def letter_grade(score):
    """0-100 puanı A-F harf notuna çevirir."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def main():
    """Ana akış: menüyü göster, seçimi işle, çıkışa kadar yinele."""
    while True:
        show_menu()
        choice = input("Seçiminiz: ")
        if choice == "1":
            weight = read_positive("Kütle (kg): ")
            height = read_positive("Boy (m): ")
            print(f"VKİ: {bmi(weight, height):.2f}")
        elif choice == "2":
            score = float(input("Puan (0-100): "))
            print(f"Harf notu: {letter_grade(score)}")
        elif choice == "0":
            print("Görüşmek üzere!")
            break
        else:
            print("Geçersiz seçim.")


main()                          # program buradan başlar
