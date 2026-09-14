# w08-10-faiz.py — bileşik faiz: birikim kaç yılda ikiye katlanır?

principal = float(input("Ana para (TL): "))
rate = float(input("Yıllık faiz (%): ")) / 100

balance = principal
years = 0
while balance < 2 * principal:         # hedef: ana paranın iki katı
    balance = balance * (1 + rate)     # yıl sonunda faiz eklenir
    years += 1
    print(f"{years:>2}. yıl sonu: {balance:>12,.2f} TL")

print(f"Para {years} yılda ikiye katlandı.")
print(f"72 kuralı tahmini: {72 / (rate * 100):.1f} yıl")
