# w06-11-sifre-kontrolu.py — şifre kuralları: metotlar + and/or

password = input("Yeni şifre: ")

# Her kural ayrı bir bool değişkende: koşul okunur hâle gelir
long_enough = len(password) >= 8
not_only_letters = not password.isalpha()
not_only_digits = not password.isdigit()
has_upper = password != password.lower()
no_space = " " not in password

ok = (long_enough and not_only_letters and not_only_digits
      and has_upper and no_space)

if ok:
    print("Şifre kabul edildi.")
elif not long_enough:
    print(f"Reddedildi: 8 karakter gerek, {len(password)} var.")
elif not (not_only_letters and not_only_digits):
    print("Reddedildi: hem harf hem rakam bulunmalı.")
elif not has_upper:
    print("Reddedildi: en az bir büyük harf bulunmalı.")
else:
    print("Reddedildi: boşluk kullanılamaz.")
