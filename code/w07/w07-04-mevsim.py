# w07-04-mevsim.py — match-case: sabit desenler ve | ile birleştirme

month = int(input("Ay numarası (1-12): "))

match month:
    case 12 | 1 | 2:
        season = "Kış"
    case 3 | 4 | 5:
        season = "İlkbahar"
    case 6 | 7 | 8:
        season = "Yaz"
    case 9 | 10 | 11:
        season = "Sonbahar"
    case _:                          # hiçbiri eşleşmediyse
        season = "geçersiz ay"

print(f"{month}. ay: {season}")
