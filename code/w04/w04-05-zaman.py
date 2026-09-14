# w04-05-zaman.py — Tam bölme (//) ve kalan (%) ile saniyeyi saat:dakika:saniye yapma

total_seconds = int(input("Toplam saniye: "))

hours = total_seconds // 3600            # 3600 saniyede bir saat
remaining = total_seconds % 3600         # saatlerden artan saniye
minutes = remaining // 60
seconds = remaining % 60

print(total_seconds, "saniye =", hours, "saat", minutes, "dakika", seconds, "saniye")

# Kontrol: parçaları birleştirip aynı sayıyı geri elde etmeliyiz
check = hours * 3600 + minutes * 60 + seconds
print("Kontrol:", check == total_seconds)
