# w13-07-fonksiyon-liste.py — Fonksiyona liste geçirmek

def add_bonus(scores, bonus):
    """Listeyi YERİNDE değiştirir; değer döndürmez (yan etki)."""
    for i in range(len(scores)):
        scores[i] = min(scores[i] + bonus, 100)


def with_bonus(scores, bonus):
    """Özgün listeye dokunmaz; YENİ liste döndürür."""
    return [min(s + bonus, 100) for s in scores]


grades = [72, 85, 91, 58, 97]
print("add_bonus dönüşü:", add_bonus(grades, 5))   # None!
print("grades           :", grades)                # değişti

safe = [72, 85, 91, 58, 97]
print("with_bonus dönüşü:", with_bonus(safe, 5))
print("safe             :", safe)                  # dokunulmadı
