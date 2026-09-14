# w12-05-fibonacci.py — Fibonacci: özyineleme, döngü, çağrı sayısı

calls = 0                           # her çağrıda artan sayaç (ölçüm için)


def fib(n):
    """n. Fibonacci sayısı: fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2)"""
    global calls
    calls += 1
    if n < 2:                       # iki taban durumu: 0 ve 1
        return n
    return fib(n - 1) + fib(n - 2)  # kendini İKİ kez çağırır


def fib_loop(n):
    """Aynı dizi döngüyle: son iki değeri taşı."""
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


print("İlk 12 Fibonacci sayısı:", end=" ")
for n in range(12):
    print(fib_loop(n), end=" ")
print()
print(f"{'n':>3} {'fib(n)':>8} {'özyineleme':>14} {'döngü':>9}")
for n in (5, 10, 20, 30):
    calls = 0
    print(f"{n:>3} {fib(n):>8} {calls:>18} {n:>11}")
