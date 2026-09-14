# w06-04-harf-notu.py — if-elif-else zinciri: 100'lük nottan harf notu

score = float(input("Dönem sonu notu (0-100): "))

if score >= 90:
    grade = "AA"
elif score >= 85:
    grade = "BA"
elif score >= 80:
    grade = "BB"
elif score >= 75:
    grade = "CB"
elif score >= 70:
    grade = "CC"
elif score >= 65:
    grade = "DC"
elif score >= 60:
    grade = "DD"
elif score >= 50:
    grade = "FD"
else:
    grade = "FF"

print(f"Not: {score:.1f} -> Harf notu: {grade}")
