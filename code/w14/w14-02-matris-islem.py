# w14-02-matris-islem.py — transpoz ve matris çarpımı

def transpose(m):
    """t[j][i] = m[i][j]; boyut ters: r x c -> c x r."""
    t = [[0] * len(m) for _ in range(len(m[0]))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            t[j][i] = m[i][j]
    return t

def multiply(a, b):
    """a (r x n) ile b (n x c) çarpımı; sonuç r x c."""
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8], [9, 10], [11, 12]]
print("Satır toplamları:", [sum(row) for row in a])
print("Sütun toplamları:", [sum(c) for c in transpose(a)])
print("Transpoz:", transpose(a))
print("a x b   :", multiply(a, b))

assert transpose(transpose(a)) == a             # 12. hafta: assert
assert sum([sum(r) for r in a]) == sum([sum(c) for c in transpose(a)])
print("Kontroller geçti.")
