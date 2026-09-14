# w12-10-tc-dogrula.py — 11 haneli kimlik numarası doğrulayıcısı
# NOT: Numaralar gerçek kişilere ait değil, sınama için kurgusaldır.

def is_valid_tc(number):
    """Biçimi ve iki kontrol basamağını doğrular.

    10. hane = ((1,3,5,7,9. haneler)*7 - (2,4,6,8. haneler)) % 10
    11. hane = (ilk 10 hanenin toplamı) % 10
    """
    if len(number) != 11 or not number.isdigit() or number[0] == "0":
        return False
    odd_sum = 0                  # 1,3,5,7,9. haneler (indeks 0,2,4,6,8)
    even_sum = 0                 # 2,4,6,8. haneler   (indeks 1,3,5,7)
    for i in range(0, 9, 2):
        odd_sum += int(number[i])
    for i in range(1, 8, 2):
        even_sum += int(number[i])
    if (odd_sum * 7 - even_sum) % 10 != int(number[9]):
        return False
    return (odd_sum + even_sum + int(number[9])) % 10 == int(number[10])


def describe(number):
    """Sonucu okunur metne çevirir (yorum katmanı)."""
    return "geçerli" if is_valid_tc(number) else "GEÇERSİZ"


def show(number):
    """Numarayı ve sonucu hizalı yazar (sunum katmanı)."""
    print(f"{number:>12}: {describe(number)}")


for tc in ("12345678950", "10000000146", "12345678901",
           "0234567895", "123a"):
    show(tc)
print("Girdiğiniz numara", describe(input("Numara girin: ").strip()))
