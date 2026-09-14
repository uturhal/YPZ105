# w15-01-yazma.py — dosyaya yazma: write, print(file=), writelines

# 1) Klasik yol: aç - yaz - kapat
f = open("selam.txt", "w", encoding="utf-8")
f.write("Merhaba dosya!\n")
f.write("Bu satırı Python yazdı.\n")
f.close()                            # kapatmayı unutmayın!

# 2) Önerilen yol: with bloğu; blok bitince dosya kendiliğinden kapanır
names = ["Ali", "Elif", "Kerem"]
with open("isimler.txt", "w", encoding="utf-8") as f:
    f.write("Ayşe")                  # write() satır sonu EKLEMEZ
    f.write("Mehmet\n")              # \n'yi biz koyarız
    print("Zeynep", file=f)          # print() satır sonunu kendi ekler
    f.writelines([name + "\n" for name in names])   # listeyi yazar

# Yazdıklarımızı geri okuyup denetleyelim
with open("selam.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")

with open("isimler.txt", encoding="utf-8") as f:    # "r" varsayılandır
    content = f.read()
print(repr(content))                 # \n karakterleri görünür olsun
print(content, end="")
