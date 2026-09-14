# w08-07-basamak.py — basamak toplamı, sayısı ve tersi

n = int(input("Pozitif bir tam sayı girin: "))
original = n                   # n döngüde tükenecek; aslını sakla

digit_sum = 0
digit_count = 0
reversed_n = 0
while n > 0:
    digit = n % 10             # son basamak
    digit_sum += digit
    digit_count += 1
    reversed_n = reversed_n * 10 + digit
    n //= 10                   # son basamağı at

print(f"{original} sayısının basamak toplamı: {digit_sum}")
print(f"Basamak sayısı: {digit_count}")
print(f"Tersi: {reversed_n}")
