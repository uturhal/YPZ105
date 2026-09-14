# w06-09-hesap-makinesi.py — dört işlem; sıfıra bölme kontrolü

x = float(input("Birinci sayı: "))
op = input("İşlem (+, -, *, /): ")
y = float(input("İkinci sayı: "))

if op == "+":
    print(f"{x} + {y} = {x + y}")
elif op == "-":
    print(f"{x} - {y} = {x - y}")
elif op == "*":
    print(f"{x} * {y} = {x * y}")
elif op == "/" and y == 0:           # genel bölme dalından ÖNCE
    print("Hata: sıfıra bölme tanımsızdır.")
elif op == "/":
    print(f"{x} / {y} = {x / y}")
else:
    print(f"Tanınmayan işlem: {op}")
