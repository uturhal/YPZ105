# w06-02-ilk-if.py — tek bir if: koşul doğruysa blok çalışır, yoksa atlanır

score = float(input("Sınav notunuz: "))

if score < 50:
    print("Uyarı: not 50'nin altında.")
    print("Ders sorumlusuyla görüşmeniz önerilir.")

print(f"Girilen not: {score:.1f}")   # girintisiz: her durumda çalışır
print("Program bitti.")
