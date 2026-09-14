# w07-09-vergi.py — Kademeli gelir vergisi (dilimler KURGUSAL, gerçek değil)
# 100 000'e kadar %15; 250 000'e kadar %20; 600 000'e kadar %27; üzeri %35 —
# her oran yalnız kendi dilimine düşen kısma uygulanır.  Sınırlarda biriken
# vergi sırasıyla 15 000, 45 000 ve 139 500 TL'dir.
income = float(input("Yıllık gelir (TL): "))

if income <= 0:
    print("Hata: gelir pozitif bir sayı olmalı.")
else:
    if income <= 100_000:
        tax = income * 0.15
    elif income <= 250_000:
        tax = 15_000 + (income - 100_000) * 0.20
    elif income <= 600_000:
        tax = 45_000 + (income - 250_000) * 0.27
    else:
        tax = 139_500 + (income - 600_000) * 0.35
    print(f"Gelir  : {income:>12,.2f} TL")
    print(f"Vergi  : {tax:>12,.2f} TL")
    print(f"Net    : {income - tax:>12,.2f} TL")
    print(f"Efektif oran: {tax / income * 100:.2f} %")
