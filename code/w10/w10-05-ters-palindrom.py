# w10-05-ters-palindrom.py — Kelimeyi döngüyle tersleme ve palindrom testi

for _ in range(2):                          # iki kelime sınayacağız
    word = input("Bir kelime: ").lower()

    reversed_word = ""                      # her karakteri BAŞA ekle
    for ch in word:
        reversed_word = ch + reversed_word

    is_palindrome = True                    # baştan ve sondan karşılaştır
    n = len(word)
    for i in range(n // 2):
        if word[i] != word[n - 1 - i]:
            is_palindrome = False
            break                           # tek uyumsuzluk yeter
    print(f"  tersi            : {reversed_word}")
    print(f"  dilimle aynı mı  : {reversed_word == word[::-1]}")
    print(f"  palindrom mu     : {is_palindrome}")
