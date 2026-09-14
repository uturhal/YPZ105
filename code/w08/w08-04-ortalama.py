# w08-04-ortalama.py — nöbetçi değerle biten döngü: -1 girilince dur

print("Notları girin; bitirmek için -1 yazın.")
total = 0
count = 0
highest = 0                          # geçici; ilk notta değişir

grade = float(input("Not: "))        # (1) ilk okuma döngüden ÖNCE
while grade != -1:                   # (2) nöbetçi değer geldi mi?
    if count == 0 or grade > highest:    # ilk not ya da yeni rekor
        highest = grade
    total += grade
    count += 1
    grade = float(input("Not: "))    # (3) SON satır: yeni okuma

if count == 0:
    print("Hiç not girilmedi.")
else:
    print(f"{count} not girildi. Ortalama: {total / count:.2f}")
    print(f"En yüksek not: {highest}")
