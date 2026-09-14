# w05-09-eposta.py — E-posta adresini döngüsüz ve if'siz denetleme

email = input("E-posta adresi: ").strip().lower()

at_pos = email.find("@")
username = email[:at_pos]
domain = email[at_pos + 1:]

print("Kullanıcı adı :", username)
print("Alan adı      :", domain)
print()
print("Tam bir @ var           :", email.count("@") == 1)
print("Kullanıcı adı boş değil :", len(username) > 0)
print("Alan adında nokta var   :", "." in domain)
print("Boşluk içermiyor        :", " " not in email)
print("Kurumsal (.edu.tr)      :", email.endswith(".edu.tr"))
