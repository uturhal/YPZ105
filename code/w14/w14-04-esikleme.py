# w14-04-esikleme.py — gri seviye görüntü = piksel matrisi; eşikleme

image = [[ 20,  35, 210,  40,  25],       # 0 siyah, 255 beyaz
         [ 30,  45, 220,  50,  35],
         [200, 215, 235, 205, 190],
         [ 25,  40, 225,  45,  30],
         [ 15,  30, 215,  35,  20]]
THRESHOLD = 128

def threshold(img, t):
    """t ve üstü 1, altı 0; YENİ bir görüntü döndürür."""
    result = []
    for row in img:
        result.append([1 if p >= t else 0 for p in row])
    return result

total = 0
brightest = 0
for row in image:
    total += sum(row)
    brightest = max(brightest, max(row))
pixels = len(image) * len(image[0])
print(f"{pixels} piksel, ortalama parlaklık {total / pixels:.1f}, "
      f"en parlak {brightest}")

binary = threshold(image, THRESHOLD)
white = 0
for row in binary:
    white += sum(row)
print(f"Eşik {THRESHOLD} ile {white} beyaz piksel:")
for row in binary:
    print("".join(["#" if p == 1 else "." for p in row]))
