# w13-10-siralama.py — Kabarcık ve seçmeli sıralama; adım sayıları

def bubble_sort(items):
    """Komşuları karşılaştırıp ters sıradaysa takas eder; yerinde."""
    comparisons = swaps = 0
    for i in range(len(items) - 1):          # geçiş numarası
        for j in range(len(items) - 1 - i):  # sondaki i eleman yerinde
            comparisons += 1
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swaps += 1
    return comparisons, swaps


def selection_sort(items):
    """Kalan kısmın en küçüğünü bulup başa taşır; yerinde."""
    comparisons = swaps = 0
    for i in range(len(items) - 1):
        smallest = i
        for j in range(i + 1, len(items)):
            comparisons += 1
            if items[j] < items[smallest]:
                smallest = j
        if smallest != i:
            items[i], items[smallest] = items[smallest], items[i]
            swaps += 1
    return comparisons, swaps


data = [64, 25, 12, 22, 11, 90, 45, 33, 78, 5]
a, b = data[:], data[:]            # kopyalar: özgün liste bozulmasın
c1, s1 = bubble_sort(a)
c2, s2 = selection_sort(b)
print("kabarcık:", a, f"| {c1} karşılaştırma, {s1} takas")
print("seçmeli :", b, f"| {c2} karşılaştırma, {s2} takas")
print("Kontrol :", a == b == sorted(data), "| özgün:", data)
