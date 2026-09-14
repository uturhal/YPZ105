# w08-11-menu.py — tekrarlı menü (ATM): while True, break ve continue

balance = 1000.0
while True:
    print("1) Bakiye  2) Para yatır  3) Para çek  4) Çıkış")
    choice = input("Seçiminiz: ")
    if choice == "4":
        print("İyi günler!")
        break                              # döngüden çık, biter
    if choice == "1":
        print(f"Bakiyeniz: {balance:.2f} TL")
    elif choice == "2":
        amount = float(input("Yatırılacak tutar: "))
        balance += amount
    elif choice == "3":
        amount = float(input("Çekilecek tutar: "))
        if amount > balance:
            print("Yetersiz bakiye!")
            continue                       # kalanı atla, menüye dön
        balance -= amount
    else:
        print("Geçersiz seçim.")
        continue
    print(f"İşlem tamam. Güncel bakiye: {balance:.2f} TL")
