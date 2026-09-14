# w12-09-test-assert.py — assert ve test fonksiyonlarıyla sınama

def letter_grade(score):
    """0-100 arası puanı harf notuna çevirir."""
    if score >= 90:
        return "AA"
    if score >= 70:
        return "BB"
    if score >= 50:
        return "CC"
    return "FF"


def is_palindrome(text):
    """Boşlukları ve harf büyüklüğünü yok sayar.

    >>> is_palindrome("Trabzon")
    False
    """
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def test_letter_grade():
    assert letter_grade(100) == "AA"
    assert letter_grade(90) == "AA"          # sınır: tam eşikte
    assert letter_grade(89.9) == "BB"        # sınır: bir altında
    assert letter_grade(50) == "CC"
    assert letter_grade(49) == "FF"
    print("test_letter_grade: geçti")


def test_is_palindrome():
    assert is_palindrome("Kayak") is True    # harf büyüklüğü
    assert is_palindrome("") is True         # uç durum: boş metin
    assert is_palindrome("Trabzon") is False
    print("test_is_palindrome: geçti")


test_letter_grade()
test_is_palindrome()
