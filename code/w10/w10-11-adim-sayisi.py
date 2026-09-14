# w10-11-adim-sayisi.py — Tek ve iç içe döngünün adım sayısını sayaçla ölçme

print(f"{'n':>5}{'tek döngü':>12}{'iç içe döngü':>15}{'oran':>7}")
for n in range(100, 501, 100):
    single = 0
    for i in range(n):
        single += 1                     # gövde her çalışmada 1 adım sayılır

    nested = 0
    for i in range(n):
        for j in range(n):
            nested += 1

    print(f"{n:>5}{single:>12}{nested:>15}{nested // single:>7}")
