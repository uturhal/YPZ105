# w13-03-sorgula-sirala.py — Üyelik, arama, sayma, sıralama

rolls = [4, 6, 2, 6, 3, 6, 1, 2]         # 8 zar atışı

print("6 var mı:", 6 in rolls, "| ilk 6:", rolls.index(6))
print("kaç tane 6:", rolls.count(6), "| eleman:", len(rolls))
print("min:", min(rolls), "max:", max(rolls), "toplam:", sum(rolls))

print("sorted():", sorted(rolls), "| özgün:", rolls)
rolls.sort()                             # YERİNDE sıralar; None döndürür
print("sort()  :", rolls)
rolls.sort(reverse=True)                 # azalan sıra
print("azalan  :", rolls)
rolls.reverse()                          # ters çevirir, sıralamaz
print("reverse():", rolls)

names = ["Zeynep", "ali", "Mert", "ayşe"]      # key= ile harf büyüklüğü
print(sorted(names), sorted(names, key=str.lower))
