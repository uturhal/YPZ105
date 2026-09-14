# w14-01-matris-temel.py — iç içe liste: erişim ve iç içe döngüyle gezinme

m = [[3, 8, 1, 6],                  # 3 satır, 4 sütun
     [5, 2, 9, 4],
     [7, 0, 3, 8]]

print("Satır sayısı:", len(m), " Sütun sayısı:", len(m[0]))
print("1. satır:", m[1])            # bir satır = bir liste
print("m[1][2] =", m[1][2], " sağ alt:", m[-1][-1])

# Bir sütunu toplamak: sütun indisi sabit, satırlar üzerinde döngü
col_total = 0
for row in m:
    col_total += row[2]
print("2. sütunun toplamı:", col_total)

# Tüm elemanları gezmek: dış döngü satır, iç döngü sütun
total = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        total += m[i][j]
print("Tüm elemanların toplamı:", total)

# İndis gerekmiyorsa aynı gezinmenin daha okunaklı biçimi
count_even = 0
for row in m:
    for value in row:
        if value % 2 == 0:
            count_even += 1
print("Çift eleman sayısı:", count_even)

m[2][1] = 10                        # tek bir hücreyi değiştirme
print("Yeni 2. satır:", m[2])
