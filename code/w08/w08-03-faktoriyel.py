# w08-03-faktoriyel.py — iki biriktirici: 1 + 2 + ... + n ve n!

n = int(input("n: "))

total = 0                # toplam biriktiricisi 0'dan başlar
product = 1              # çarpım biriktiricisi 1'den başlar (0 değil!)
i = 1
while i <= n:
    total += i           # total = total + i
    product *= i         # product = product * i
    i += 1

print(f"1 + 2 + ... + {n} = {total}")
print(f"{n}! = {product}")
