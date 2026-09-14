# w12-06-us-alma.py — Üs alma: döngü ve hızlı özyineleme

mults = 0                           # ölçüm sayacı: kaç çarpma yapıldı?


def power_loop(base, exponent):
    """Döngüyle: exponent kez çarpar."""
    global mults
    result = 1
    for _ in range(exponent):
        result *= base
        mults += 1
    return result


def power_fast(base, exponent):
    """Hızlı üs alma: üs her adımda YARIYA iner."""
    global mults
    if exponent == 0:               # taban durumu
        return 1
    half = power_fast(base, exponent // 2)
    mults += 1
    if exponent % 2 == 0:
        return half * half
    mults += 1
    return half * half * base


print(f"{'n':>3} {'2**n':>22} {'döngü':>7} {'hızlı':>7}")
for n in (10, 20, 40, 64):
    counts = []
    for power in (power_loop, power_fast):
        mults = 0
        assert power(2, n) == 2 ** n     # ikisi de aynı sayıyı vermeli
        counts.append(mults)
    print(f"{n:>3} {2 ** n:>22} {counts[0]:>7} {counts[1]:>7}")
