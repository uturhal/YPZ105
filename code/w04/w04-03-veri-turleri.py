# w04-03-veri-turleri.py — Temel veri türleri ve type() işlevi

count = 12              # int   : tam sayı
price = 49.90           # float : ondalıklı (kayan noktalı) sayı
city = "Trabzon"        # str   : karakter dizisi (metin)
is_open = False         # bool  : mantıksal değer (True / False)

print(count, "->", type(count))
print(price, "->", type(price))
print(city, "->", type(city))
print(is_open, "->", type(is_open))

# Metin ve sayı aynı şey değildir: "12" bir metindir, 12 bir sayıdır.
text_number = "12"
print(text_number + text_number)    # metinler birleştirilir  -> 1212
print(count + count)                # sayılar toplanır        -> 24

# int sınırsız büyüklükte olabilir
big = 2 ** 100
print("2 üzeri 100 =", big)

# float her ondalık sayıyı tam tutamaz
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3 ?", 0.1 + 0.2 == 0.3)
print("Yuvarlayarak karşılaştırma:", round(0.1 + 0.2, 10) == 0.3)
