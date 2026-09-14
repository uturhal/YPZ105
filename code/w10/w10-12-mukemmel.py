# w10-12-mukemmel.py — 1–1000 arası mükemmel sayılar (bölen toplamı = sayı)
LIMIT = 1000
for number in range(2, LIMIT + 1):
    divisor_sum = 0
    divisors_text = ""
    for divisor in range(1, number // 2 + 1):   # en büyük bölen: n/2
        if number % divisor == 0:
            divisor_sum += divisor
            divisors_text += f"{divisor} + "
    if divisor_sum == number:
        print(f"{number} = {divisors_text[:-3]}")  # sondaki ' + ' atılır
