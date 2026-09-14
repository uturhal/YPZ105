# w08-12-asal.py — asal testi: while ... else ve i * i <= n sınırı

n = int(input("Bir tam sayı girin: "))

i = 2
while i * i <= n:              # bölen aramak için √n'e kadar yeter
    if n % i == 0:
        print(f"{n} asal değildir: {n} = {i} x {n // i}")
        break                  # bölen bulundu; else bloğu ATLANIR
    i += 1
else:                          # döngü break OLMADAN bittiyse çalışır
    if n >= 2:
        print(f"{n} asaldır ({i - 2} bölen denendi).")
    else:
        print(f"{n} asal değildir; asallar 2'den başlar.")
