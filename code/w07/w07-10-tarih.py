# w07-10-tarih.py — Tarih geçerliliği: gün/ay/yıl + artık yıl (6. hafta)

day = int(input("Gün: "))
month = int(input("Ay: "))
year = int(input("Yıl: "))

is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

if month < 1 or month > 12:
    print(f"Geçersiz: {month}. ay yok.")
else:
    match month:                             # ayın kaç gün çektiği
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            days_in_month = 31
        case 4 | 6 | 9 | 11:
            days_in_month = 30
        case 2:
            days_in_month = 29 if is_leap else 28
    if 1 <= day <= days_in_month:
        print(f"{day:02d}.{month:02d}.{year} geçerli bir tarih.")
    else:
        print(f"Geçersiz: {year} yılında {month}. ay {days_in_month} gün.")
