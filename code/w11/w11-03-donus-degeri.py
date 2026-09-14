# w11-03-donus-degeri.py — return ile değer döndürme (sıcaklık, VKİ)

def celsius_to_fahrenheit(celsius):
    """Celsius sıcaklığı Fahrenheit'a çevirir."""
    return celsius * 9 / 5 + 32


def bmi(weight, height):
    """Vücut kitle indeksi: kütle (kg) / boy (m) karesi."""
    return weight / height ** 2


# 1) Dönüş değeri bir değişkene atanır
f = celsius_to_fahrenheit(37)
print("37 °C =", f, "°F")

# 2) Doğrudan bir ifadenin içinde kullanılır
print("Kaynama - donma farkı:",
      celsius_to_fahrenheit(100) - celsius_to_fahrenheit(0), "°F")

# 3) f-string içinde biçimlenir
print(f"VKİ: {bmi(70, 1.75):.2f}")

# 4) Bir karşılaştırmanın parçası olur
print("Normal aralıkta mı?", bmi(70, 1.75) < 25)
