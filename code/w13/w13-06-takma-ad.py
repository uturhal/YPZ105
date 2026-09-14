# w13-06-takma-ad.py — Takma ad (aynı nesne) ile kopya (ayrı nesne)

a = [1, 2, 3]
b = a                # kopya DEĞİL: aynı nesneye takılan ikinci etiket
b.append(4)
print("a =", a, " b =", b, "| a is b:", a is b)

c = a[:]             # dilimleme yeni liste üretir → gerçek kopya
d = list(a)          # aynı iş; a.copy() de aynı
c[0] = 99
print("a =", a, " c =", c)
print("a is c:", a is c, "| a == c:", a == c, "| a == d:", a == d)

x = 5                # sayı değiştirilemez: takma ad sorunu çıkmaz
y = x
y += 1               # y YENİ bir int nesnesine bağlanır
print("x =", x, " y =", y)
