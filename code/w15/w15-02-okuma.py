# w15-02-okuma.py — bir metin dosyasını okumanın dört yolu

# 1) read(): tüm dosya tek bir metin (str) olarak
with open("siir.txt", encoding="utf-8") as f:
    text = f.read()
print(type(text), len(text), "karakter")
print(text[:33] + "...")

# 2) readline(): her çağrıda bir satır; satır sonu \n dahildir
with open("siir.txt", encoding="utf-8") as f:
    first = f.readline()
    second = f.readline()
print(repr(first))
print(repr(second.strip()))          # strip() \n'yi atar

# 3) readlines(): tüm satırlar bir listede
with open("siir.txt", encoding="utf-8") as f:
    lines = f.readlines()
print(len(lines), "satır; sonuncusu:", repr(lines[-1]))

# 4) for satır in dosya: en iyi yol (hepsini belleğe almaz)
with open("siir.txt", encoding="utf-8") as f:
    for number, line in enumerate(f, start=1):
        print(f"{number:2d}: {line.strip()}")
