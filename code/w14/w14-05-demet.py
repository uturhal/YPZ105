# w14-05-demet.py — demet: değiştirilemez dizi, paketleme ve açma

point = (3, 4)
print(point, type(point), " x =", point[0], " uzunluk:", len(point))

single = (5,)                  # tek elemanlı demet: virgül şart!
not_tuple = (5)                # bu yalnız parantezli bir sayıdır
print(type(single), type(not_tuple))

trabzon = 41.0027, 39.7168     # paketleme: parantez gerekmez
lat, lon = trabzon             # açma
print(f"Enlem: {lat}  Boylam: {lon}")

a, b = 3, 8
a, b = b, a                    # takas: sağda paketle, solda aç
print("a =", a, " b =", b)

def divide(x, y):
    """Bölümü ve kalanı birlikte, demet olarak döndürür."""
    return x // y, x % y

q, r = divide(17, 5)           # dönen demet açılır
print(f"17 = {q} * 5 + {r}")

colors = ("kırmızı", "yeşil", "mavi")
color_list = list(colors)      # listeye çevir, değiştir, geri çevir
color_list.append("sarı")
colors = tuple(color_list)     # YENİ bir demet; eskisi değişmedi
print(colors, len(colors), colors.count("sarı"), colors.index("mavi"))
