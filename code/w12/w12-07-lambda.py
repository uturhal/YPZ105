# w12-07-lambda.py — Adsız fonksiyonlar ve key parametresi

def square_def(x):                       # aynı işi yapan iki tanım
    return x * x


square = lambda x: x * x

print(square_def(7), square(7))

# key: karşılaştırma ÖNCESİ her elemana uygulanan fonksiyon
print(max(3, -7, 5))                     # olduğu gibi en büyük
print(max(3, -7, 5, key=abs))            # mutlak değeri en büyük olan
print(min("Trabzon", "Ankara", "İzmir", key=len))   # en kısa metin

# Karakterleri sıralama: büyük harfler Unicode'da küçüklerden önce gelir
word = "PythOn"
print("".join(sorted(word)))                          # 'O' ve 'P' başa
print("".join(sorted(word, key=lambda c: c.lower())))  # harf sırası
