# w04-02-degiskenler.py — Değişkenler ve atama

# Atama: sağdaki değer hesaplanır, soldaki ada bağlanır.
student_name = "Ayşe Yılmaz"
student_no = 2026105017
midterm = 72.5
is_passing = True

print("Ad Soyad :", student_name)
print("Numara   :", student_no)
print("Vize notu:", midterm)
print("Geçiyor mu?", is_passing)

# Bir değişkenin değeri sonradan değiştirilebilir (variable = değişebilen).
midterm = 85.0
print("Yeni vize notu:", midterm)

# Çoklu atama ve iki değişkenin değerini takas etme
a, b = 3, 8
print("Önce : a =", a, " b =", b)
a, b = b, a
print("Sonra: a =", a, " b =", b)

# Sabitler: değişmemesi gereken değerler BÜYÜK HARFLE yazılır (bir gelenektir,
# Python zorlamaz).
PI = 3.14159
GRAVITY = 9.81
print("Yerçekimi ivmesi:", GRAVITY, "m/s^2")
