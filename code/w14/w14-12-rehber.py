# w14-12-rehber.py — menülü telefon rehberi: sözlükle ekle, ara, listele

MENU = "\n1) Ekle/güncelle  2) Ara  3) Listele  0) Çık"

def add_or_update(book):
    name = input("Ad: ").strip()
    phone = input("Telefon: ").strip()
    print(f"{name} güncellendi." if name in book else f"{name} eklendi.")
    book[name] = phone              # ekleme ve güncelleme aynı yazım

def find(book):
    name = input("Aranan ad: ").strip()
    phone = book.get(name)          # yoksa None; KeyError yok
    print(f"{name}: {phone}" if phone else f"{name} rehberde yok.")

def list_all(book):
    print(f"{len(book)} kayıt:")
    for name in sorted(book):       # sözlük kendiliğinden sıralı değil
        print(f"  {name:<10} {book[name]}")

book = {"Zeynep": "0533 000 11 22"}
while True:
    print(MENU)
    choice = input("Seçiminiz: ").strip()
    if choice == "1":
        add_or_update(book)
    elif choice == "2":
        find(book)
    elif choice == "3":
        list_all(book)
    elif choice == "0":
        print("Rehber kapatıldı. Kayıt sayısı:", len(book))
        break
    else:
        print("Geçersiz seçim.")
