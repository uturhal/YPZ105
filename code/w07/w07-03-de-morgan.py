# w07-03-de-morgan.py — De Morgan kuralları, zincirleme ve "or" tuzağı

print("  a      b    | not (a and b) | not a or not b")
print("-------------+---------------+---------------")
a, b = True, True
print(f"{a!s:<6} {b!s:<6}| {not (a and b)!s:^13} | {not a or not b!s:^14}")
a, b = True, False
print(f"{a!s:<6} {b!s:<6}| {not (a and b)!s:^13} | {not a or not b!s:^14}")
a, b = False, True
print(f"{a!s:<6} {b!s:<6}| {not (a and b)!s:^13} | {not a or not b!s:^14}")
a, b = False, False
print(f"{a!s:<6} {b!s:<6}| {not (a and b)!s:^13} | {not a or not b!s:^14}")

# Aralık kontrolü: üç yazım, aynı anlam
x = 7
print(x >= 0 and x <= 10)        # klasik
print(0 <= x <= 10)              # zincirleme (tercih edilen)
print(not (x < 0 or x > 10))     # De Morgan ile eşdeğeri

# Tuzak: "x, 1 ya da 2'ye eşit mi?" demek için BU yazılmaz
print(x == 1 or 2)               # sonuç 2 -> koşulda hep doğru sayılır!
print(x == 1 or x == 2)          # doğrusu
