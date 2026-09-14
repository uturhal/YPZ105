# w14-06-kayitlar.py — demet listesi = kayıtlar; zip, çoklu dönüş, sıralama

names = ["Ayşe", "Mehmet", "Zeynep", "Can", "Elif"]
scores = [85, 60, 95, 70, 78]

records = list(zip(names, scores))   # her kayıt bir (ad, puan) demeti
print(records[:3], "...")

def summarize(recs):
    """En düşük kaydı, en yüksek kaydı ve ortalamayı döndürür."""
    lowest = highest = recs[0]
    total = 0
    for name, score in recs:         # demeti döngüde aç
        total += score
        if score < lowest[1]:
            lowest = (name, score)
        if score > highest[1]:
            highest = (name, score)
    return lowest, highest, total / len(recs)

low, high, avg = summarize(records)
print(f"En düşük: {low[0]} ({low[1]}), en yüksek: {high[0]} ({high[1]})")
print(f"Ortalama: {avg:.1f}")

# Puana göre büyükten küçüğe: anahtar, demetin 1. elemanı
by_score = sorted(records, key=lambda rec: rec[1], reverse=True)
for rank, (name, score) in enumerate(by_score, start=1):
    print(f"{rank:<3} {name:<9} {score:>4}")
print("Alfabetik ilk iki:", sorted(records)[:2])   # anahtarsız: ada göre
