# w11-04-print-vs-return.py — print ile return farkı: değer nereye gider?

def square_print(x):
    """Karesini EKRANA yazar; çağırana bir şey döndürmez."""
    print(x * x)


def square_return(x):
    """Karesini ÇAĞIRANA döndürür; ekrana bir şey yazmaz."""
    return x * x


a = square_print(4)         # 16 ekrana yazılır ...
print("a =", a)             # ... ama a'ya None gelir
print(type(a))

b = square_return(4)        # ekrana hiçbir şey yazılmaz ...
print("b =", b)             # ... değer b'de saklanır
print("b + 1 =", b + 1)     # ve hesapta kullanılabilir
print(square_return(4))     # dönen değeri BİZ yazdırıyoruz
square_return(4)            # dönen değer kullanılmadı: kaybolur
