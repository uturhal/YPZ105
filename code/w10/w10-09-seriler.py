# w10-09-seriler.py — Döngüyle biriktirilen seriler: harmonik toplam, π, e

import math

n = int(input("Terim sayısı n: "))

harmonic = 0.0                          # 1 + 1/2 + 1/3 + ... + 1/n
for k in range(1, n + 1):
    harmonic += 1 / k

pi_sum = 0.0                            # 4(1 - 1/3 + 1/5 - 1/7 + ...)
sign = 1
for k in range(n):
    pi_sum += sign / (2 * k + 1)
    sign = -sign                        # işaret her terimde değişir
pi_approx = 4 * pi_sum

e_sum = 1.0                             # k = 0 terimi: 1/0! = 1
term = 1.0
for k in range(1, n):
    term = term / k                     # 1/k! = (1/(k-1)!) / k
    e_sum += term

print(f"H({n}) = {harmonic:.6f}")
print(f"π yaklaşımı ({n} terim) = {pi_approx:.6f}   (gerçek {math.pi:.6f})")
print(f"hata                     = {abs(pi_approx - math.pi):.6f}")
print(f"e yaklaşımı ({n} terim) = {e_sum:.10f}   (gerçek {math.e:.10f})")
