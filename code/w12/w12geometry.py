# w12geometry.py — Geometri modülü (sizde: geometry.py)
"""Düzlem geometrisi yardımcıları.

Kullanım:  import w12geometry as geometry
           print(geometry.circle_area(3))
"""
import math


def circle_area(r):
    """Yarıçapı r olan dairenin alanı."""
    return math.pi * r ** 2


def circle_perimeter(r):
    """Yarıçapı r olan dairenin çevresi."""
    return 2 * math.pi * r


def rectangle_area(width, height):
    """Dikdörtgenin alanı."""
    return width * height


def square_area(side):
    """Karenin alanı; işi dikdörtgen fonksiyonuna devreder."""
    return rectangle_area(side, side)


def triangle_area(a, b, c):
    """Heron formülü; kenarlar üçgen oluşturmuyorsa 0 döndürür."""
    if a + b <= c or a + c <= b or b + c <= a:
        return 0
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


if __name__ == "__main__":          # yalnız DOĞRUDAN çalıştırılırsa
    print("w12geometry kendini test ediyor...")
    assert square_area(4) == rectangle_area(4, 4) == 16
    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(1, 2, 10) == 0
    assert abs(circle_area(1) - math.pi) < 1e-9
    print("Tüm testler geçti.")
