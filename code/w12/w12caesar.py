# w12caesar.py — Sezar şifresi modülü: encrypt / decrypt
"""Sezar şifresi: her harfi alfabede `shift` kadar ileri kaydırır.

Yalnız İngiliz alfabesindeki harfler kaydırılır; boşluk, rakam ve
noktalama olduğu gibi kalır.  Çözme, ters yöne kaydırmadır.
"""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def _shift_char(ch, shift):
    """Tek karakteri kaydırır (modül içi yardımcı; alt çizgi = iç iş)."""
    if ch.lower() not in ALPHABET:
        return ch
    index = ALPHABET.find(ch.lower())
    new_ch = ALPHABET[(index + shift) % 26]
    if ch.isupper():
        return new_ch.upper()
    return new_ch


def encrypt(text, shift=3):
    """Metni şifreler; kaydırma verilmezse 3 kullanılır."""
    result = ""
    for ch in text:
        result += _shift_char(ch, shift)
    return result


def decrypt(text, shift=3):
    """Şifreyi çözer: encrypt(text, -shift) ile aynı şeydir."""
    return encrypt(text, -shift)


if __name__ == "__main__":
    print("w12caesar kendini test ediyor...")
    assert encrypt("abc") == "def"
    assert encrypt("xyz") == "abc"                  # sondan başa dönüş
    assert encrypt("Hello, World!", 5) == "Mjqqt, Btwqi!"
    assert decrypt(encrypt("Trabzon 2026", 11), 11) == "Trabzon 2026"
    assert encrypt("python", 26) == "python"        # tam tur = değişmez
    print("Tüm testler geçti.")
    print("Örnek:", encrypt("merhaba dunya"), "->",
          decrypt(encrypt("merhaba dunya")))
