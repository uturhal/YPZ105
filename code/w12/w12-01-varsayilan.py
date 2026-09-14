# w12-01-varsayilan.py — Varsayılan ve anahtar sözcüklü argümanlar

def greet(name, greeting="Merhaba", punctuation="!"):
    """Kişiyi selamlar; selam sözcüğü ve noktalama isteğe bağlıdır."""
    print(f"{greeting}, {name}{punctuation}")


def price_with_tax(price, rate=0.20):
    """Fiyata KDV ekler; oran verilmezse %20 kullanılır."""
    return price * (1 + rate)


greet("Ayşe")                       # eksikler varsayılandan tamamlanır
greet("Mehmet", "Günaydın")         # konumsal: sıra parametre sırasıdır
greet("Ali", punctuation="...")     # anahtar sözcüklü: ada göre eşleşir
greet(greeting="Selam", name="Fatma")                # sıra serbest
greet("Can", punctuation="?", greeting="Nasılsın")   # önce konumsal
print(f"{price_with_tax(120):.2f} TL ve "
      f"{price_with_tax(15, rate=0.01):.2f} TL")

# print() de aynı kurala uyar: sep ve end varsayılanlı, anahtar sözcüklü
print("2026", "09", "13", sep="-")
print("Yükleniyor", end="")
print("... tamam")
