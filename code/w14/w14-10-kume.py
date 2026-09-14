# w14-10-kume.py — küme: benzersiz elemanlar ve küme işlemleri

numbers = [3, 7, 3, 1, 7, 7, 9, 1]
unique = set(numbers)                   # yinelenenler bir kez kalır
print(unique, len(unique), sorted(unique))
print("7 var mı?", 7 in unique, " 5 var mı?", 5 in unique)

morning = {"Ayşe", "Mehmet", "Zeynep", "Can"}
evening = {"Zeynep", "Can", "Elif"}
print("Birleşim:", sorted(morning | evening))
print("Kesişim :", sorted(morning & evening))
print("Fark    :", sorted(morning - evening))
print("Simetrik:", sorted(morning ^ evening))

morning.add("Deniz")
morning.discard("Ayşe")                 # yoksa hata vermez
print("Sabah grubu:", sorted(morning))

text = "veri veri model model model tahmin"
print(f"{len(text.split())} kelime, {len(set(text.split()))} farklı")

print(type(set()), type({}))            # boş küme set(); {} sözlüktür
