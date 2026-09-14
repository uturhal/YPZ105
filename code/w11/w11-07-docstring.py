# w11-07-docstring.py — Belgeleme dizesi (docstring) ve help()
import math


def circle_area(radius):
    """Yarıçapı verilen dairenin alanını döndürür.

    radius: yarıçap (float);  Dönüş: alan, aynı birimin karesi (float)
    """
    return math.pi * radius ** 2


print("circle_area(3) =", circle_area(3))
help(circle_area)               # kendi fonksiyonumuzun belgesi
help(len)                       # yerleşiğin belgesi de aynı yolla
