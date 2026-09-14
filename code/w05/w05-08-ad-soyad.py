# w05-08-ad-soyad.py — Ad-soyadı ayırma, biçimleme, baş harfler ve
# kullanıcı adı üretme

full_name = input("Adınızı ve soyadınızı girin: ")

clean = " ".join(full_name.split())     # fazla boşlukları at
parts = clean.split()
first_name = parts[0].capitalize()
last_name = parts[-1].capitalize()

initials = first_name[0] + "." + last_name[0] + "."
username = (first_name + "." + last_name).lower()
username = username.replace("ş", "s").replace("ı", "i")
username = username.replace("ğ", "g").replace("ç", "c")
username = username.replace("ö", "o").replace("ü", "u")

print("Ad         :", first_name)
print("Soyad      :", last_name)
print("Baş harfler:", initials)
print("Kullanıcı  :", username)
print("Uzunluk    :", len(clean), "karakter,", len(parts), "sözcük")
