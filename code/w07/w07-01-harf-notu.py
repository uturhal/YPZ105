# w07-01-harf-notu.py — İç içe if: not aralığı → devamsızlık → harf notu
# Kural (kurgusal): 14 haftada 4'ten fazla devamsızlık DZ (devamsız) sayılır

score = float(input("Dönem sonu notu (0-100): "))
absent = int(input("Devamsız hafta sayısı: "))

if 0 <= score <= 100:                 # 1. seviye: girdi geçerli mi?
    if absent > 4:                    # 2. seviye: devam koşulu
        grade = "DZ"
    else:                             # 3. seviye: not aralıkları
        if score >= 90:
            grade = "AA"
        elif score >= 80:
            grade = "BB"
        elif score >= 70:
            grade = "CC"
        elif score >= 60:
            grade = "DD"
        else:
            grade = "FF"
    print(f"Not: {score:.1f}  Devamsızlık: {absent} hafta  ->  {grade}")
else:
    print("Hata: not 0 ile 100 arasında olmalı.")
