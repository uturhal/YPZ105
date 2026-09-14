# w14-08-kelime-frekans.py — frekans sayma deseni: metin -> sözlük

text = "elma armut elma kiraz muz elma armut kiraz elma muz kivi armut"
words = text.split()

counts = {}                     # 1. biçim: önce sor, sonra artır
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

counts2 = {}                    # 2. biçim: get ile tek satır
for word in words:
    counts2[word] = counts2.get(word, 0) + 1

print(f"{len(words)} kelime, {len(counts)} farklı kelime")
print(counts)
print("İki biçim aynı sonucu verir:", counts == counts2)

# Sözlüğü (kelime, sayı) demetlerine çevirip sayıya göre sırala
pairs = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
print("En sık üç kelime:")
for word, n in pairs[:3]:
    print(f"  {word:<8} {n:>2}  {'*' * n}")
