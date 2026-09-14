# w12-02-coklu-donus.py — Birden çok değer döndürme ve *args

def divide(a, b):
    """a'yı b'ye böler; bölümü ve kalanı birlikte döndürür."""
    return a // b, a % b            # iki değer, virgülle


def stats(x, y, z):
    """Üç sayının en küçüğünü, en büyüğünü ve ortalamasını döndürür."""
    return min(x, y, z), max(x, y, z), (x + y + z) / 3


def total(*numbers):
    """Kaç tane verilirse verilsin, sayıların toplamını döndürür."""
    result = 0
    for n in numbers:               # numbers bir demettir (14. hafta)
        result += n
    return result


q, r = divide(17, 5)                # iki değeri iki ada aç
print(f"17 = {q} * 5 + {r}", "| divmod:", divmod(17, 5))
lowest, highest, average = stats(72, 91, 64)
print(f"En düşük {lowest}, en yüksek {highest}, ortalama {average:.1f}")
pair = divide(17, 5)                # tek ada atarsanız paket açılmaz
print("Tek ad:", pair, type(pair))
print(total(3, 4), total(10, 20, 30, 40), total())
