# w13-02-degistir.py — Liste değiştirilebilir: eleman atama ve metotlar

shopping = ["süt", "ekmek", "yumurta"]
shopping[1] = "kepekli ekmek"     # eleman atama: o yerin içeriği değişir
print("atama :", shopping)

shopping.append("peynir")         # sona ekle
shopping.insert(0, "su")          # indekse ekle, gerisini sağa kaydır
shopping.extend(["çay", "şeker"])  # başka listenin elemanlarını ekle
print("ekleme:", shopping)

shopping.remove("yumurta")        # DEĞERE göre sil (ilk eşleşen)
last = shopping.pop()             # SON elemanı çıkar ve döndür
first = shopping.pop(0)           # indekstekini çıkar ve döndür
del shopping[1]                   # indekstekini sil; değer döndürmez
print("silme :", shopping, "| pop:", last, first)

shopping[0:2] = ["kahve", "fındık", "bal"]  # 2 yere 3 eleman
print("dilim :", shopping, len(shopping))

shopping.clear()                  # hepsini sil; liste nesnesi boşalır
print("clear :", shopping, len(shopping))
