# w10-06-enumerate-zip.py — enumerate, zip ve reversed ile metin döngüleri

word = "PYTHON"

print("enumerate — indeks ve karakter birlikte:")
for i, ch in enumerate(word):
    print(f"{i}:{ch}", end="  ")

print("\nenumerate(start=1) — 1'den numaralandırma:")
for no, ch in enumerate(word, start=1):
    print(f"{no}. harf {ch}", end="  ")

print("\nzip — iki metni eşleştirir, kısa olanda durur:")
for plain, secret in zip("ABCDE", "DEFGHIJ"):
    print(f"{plain}->{secret}", end="  ")

print("\nreversed — sondan başa:")
for ch in reversed(word):
    print(ch, end="")
print("\naynı iş, geriye sayan range ile:")
for i in range(len(word) - 1, -1, -1):
    print(word[i], end="")
print()
