# w13-12-alisveris.py — Alışveriş listesi: menü döngüsü + liste metotları


def show(items):
    """Listeyi numaralı satırlar hâlinde yazar."""
    if len(items) == 0:
        print("  (liste boş)")
    for i, item in enumerate(items, start=1):
        print(f"  {i}. {item}")


items = []
while True:
    choice = input("[1] Ekle [2] Sil [3] Listele [4] Çık > ")
    if choice == "1":
        name = input("  Ürün: ")
        if name in items:
            print("  Zaten listede.")
        else:
            items.append(name)
    elif choice == "2":
        name = input("  Silinecek ürün: ")
        if name in items:
            items.remove(name)
        else:
            print("  Listede yok:", name)
    elif choice == "3":
        show(items)
    elif choice == "4":
        print("Son liste:", items, "| ürün sayısı:", len(items))
        break
    else:
        print("  Geçersiz seçim.")
