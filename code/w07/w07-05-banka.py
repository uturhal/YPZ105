# w07-05-banka.py — match-case ile guard (case ... if koşul): banka işlemi

balance = float(input("Mevcut bakiye (TL): "))
operation = input("İşlem (yatır / çek / bakiye): ").strip().lower()
amount = float(input("Tutar (TL, bakiye için 0): "))

match operation:
    case "yatır" | "yatir":
        balance = balance + amount
        print(f"{amount:.2f} TL yatırıldı. Yeni bakiye: {balance:.2f} TL")
    case "çek" | "cek" if amount > balance:       # guard: önce bu denenir
        print(f"Yetersiz bakiye! En fazla {balance:.2f} TL çekebilirsiniz.")
    case "çek" | "cek":                        # guard sağlanmadıysa buraya
        balance = balance - amount
        print(f"{amount:.2f} TL çekildi. Yeni bakiye: {balance:.2f} TL")
    case "bakiye":
        print(f"Bakiyeniz: {balance:.2f} TL")
    case _:
        print(f"Tanınmayan işlem: '{operation}'")
