# w13-05-en-buyuk-iki.py — Tek geçişte en büyük iki elemanı bulma

scores = [67, 89, 45, 92, 78, 83]

first = scores[0]            # şimdiye kadarki en büyük
second = None                # ikinci en büyük: henüz yok
for s in scores[1:]:         # ilk eleman zaten first'te
    if s > first:
        second = first       # eski birinci ikinciliğe iner
        first = s
    elif second is None or s > second:
        second = s
print("En büyük:", first, "İkinci:", second)

ordered = sorted(scores)     # kontrol: sondan iki eleman aynı mı?
print("Sıralı:", ordered, "|", ordered[-1], ordered[-2])
