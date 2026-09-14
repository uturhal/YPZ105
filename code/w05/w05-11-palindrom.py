# w05-11-palindrom.py — Palindrom: temizle, ters çevir, karşılaştır

text = input("Bir sözcük ya da cümle: ")

cleaned = text.lower().replace(" ", "").replace("'", "")
cleaned = cleaned.replace(",", "").replace(".", "")
reversed_text = cleaned[::-1]

print("Temizlenmiş  :", cleaned)
print("Tersi        :", reversed_text)
print("Palindrom mu?", cleaned == reversed_text)
