# w11-05-harf-notu.py — Birden çok return noktası: harf notu (erken dönüş)

def letter_grade(score):
    """0-100 arası puanı A, B, C, D, F harf notuna çevirir."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"              # hiçbir koşul tutmadıysa buraya gelinir


for score in range(100, 55, -10):
    print(f"{score:>5} -> {letter_grade(score)}")

# Sınır değerleri: 90 A verir, 89.9 B vermeli
print(f"{89.9:>5} -> {letter_grade(89.9)}")
print(f"{59.9:>5} -> {letter_grade(59.9)}")
