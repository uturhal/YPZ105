# w11-09-geometri.py — Geometri kütüphaneciği ve elle test tablosu
import math


def circle_area(r):
    """Dairenin alanı: pi * r^2"""
    return math.pi * r ** 2


def circle_perimeter(r):
    """Dairenin çevresi: 2 * pi * r"""
    return 2 * math.pi * r


def rectangle_area(width, height):
    """Dikdörtgenin alanı."""
    return width * height


def rectangle_perimeter(width, height):
    """Dikdörtgenin çevresi."""
    return 2 * (width + height)


# Test tablosu: bilinen girdi -> beklenen çıktı
print(f"{'Çağrı':<26}{'Sonuç':>9}{'Beklenen':>10}")
print("-" * 45)
print(f"{'circle_area(1)':<26}{circle_area(1):>9.4f}{3.1416:>10.4f}")
print(f"{'circle_area(3)':<26}{circle_area(3):>9.2f}{28.27:>10.2f}")
c = circle_perimeter(3)
print(f"{'circle_perimeter(3)':<26}{c:>9.2f}{18.85:>10.2f}")
print(f"{'rectangle_area(3, 4)':<26}{rectangle_area(3, 4):>9}{12:>10}")
p = rectangle_perimeter(3, 4)
print(f"{'rectangle_perimeter(3, 4)':<26}{p:>9}{14:>10}")
