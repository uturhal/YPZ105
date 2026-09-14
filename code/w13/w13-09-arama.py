# w13-09-arama.py — Doğrusal arama ile ikili arama: adım karşılaştırması

def linear_search(items, target):
    """Baştan sona bakar; (indeks, adım) döndürür, yoksa (-1, n)."""
    for i in range(len(items)):
        if items[i] == target:
            return i, i + 1        # i + 1 = yapılan karşılaştırma sayısı
    return -1, len(items)


def binary_search(items, target):
    """SIRALI listeyi ortadan böler; (indeks, adım) döndürür."""
    low, high, steps = 0, len(items) - 1, 0
    while low <= high:
        mid = (low + high) // 2
        steps += 1
        if items[mid] == target:
            return mid, steps
        elif items[mid] < target:
            low = mid + 1          # hedef sağ yarıda
        else:
            high = mid - 1         # hedef sol yarıda
    return -1, steps


data = [4, 9, 15, 23, 31, 42, 57, 68]
for target in [57, 4, 50]:
    i1, s1 = linear_search(data, target)
    i2, s2 = binary_search(data, target)
    print(f"hedef {target:>2}: doğrusal {i1:>2} ({s1} adım)"
          f" | ikili {i2:>2} ({s2} adım)")

big = list(range(0, 200000, 2))    # 100 000 sıralı çift sayı
print("n =", len(big), "| doğrusal:", linear_search(big, 199998),
      "| ikili:", binary_search(big, 199998))
