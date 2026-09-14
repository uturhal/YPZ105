# w15-05-sayac.py — ziyaretçi sayacı: oku, artır, yaz (dosya yoksa oluştur)
import os

COUNTER_FILE = "sayac.txt"


def visit():
    """Sayacı bir artırır, yeni değeri dosyaya yazar ve döndürür."""
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, encoding="utf-8") as f:
            count = int(f.read().strip())
    else:
        count = 0                    # ilk ziyaret: dosya henüz yok
    count += 1
    with open(COUNTER_FILE, "w", encoding="utf-8") as f:
        f.write(str(count))          # write() sayı kabul etmez: str()
    return count


# Programın üç kez çalıştırılmasını taklit ediyoruz
for run in range(3):
    print(f"Hoş geldiniz! Siz {visit()}. ziyaretçisiniz.")

with open(COUNTER_FILE, encoding="utf-8") as f:
    print("Dosyanın son içeriği:", repr(f.read()))
