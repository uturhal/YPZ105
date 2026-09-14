# w05-05-split-join.py — split ile parçalama, join ile birleştirme,
# kelime sayma

full_name = "Ayşe Nur Yılmaz"
parts = full_name.split()          # boşluklardan böler
print(parts, len(parts), "parça")
print("İlk:", parts[0], "| Son:", parts[-1])

# Ayırıcı verilebilir; parça sayısı belliyse çoklu atama
date = "13/09/2026"
day, month, year = date.split("/")
print(year + "-" + month + "-" + day)

record = "2026105017;Ayşe;Yılmaz;85.5"
fields = record.split(";")
print(fields[1], fields[2], "->", float(fields[3]) + 4.5)

# join: parçaları verilen ayırıcıyla birleştirir (split'in tersi)
print(" ".join(parts), "|", "-".join(parts))

# Uygulama: kelime sayma ve fazla boşlukları temizleme
text = "Yapay zeka  bilgisayarların   öğrenmesini sağlar"
print(len(text.split()), len(text.split(" ")))   # 5 ve 8!
print(" ".join(text.split()))         # tek boşluklu temiz metin
