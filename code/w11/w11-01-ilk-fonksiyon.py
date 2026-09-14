# w11-01-ilk-fonksiyon.py — İlk fonksiyon: tanım, çağrı ve çalışma sırası

def print_header():
    """Üç satırlık bir başlık yazar."""
    print("=" * 30)
    print("   YPZ105 - Fonksiyonlar")
    print("=" * 30)


# Ana program buradan başlar; yukarıdaki tanım henüz hiçbir şey yazdırmadı.
print("1) Ana program başladı.")
print_header()                  # çağrı: akış gövdeye atlar, sonra döner
print("2) İlk çağrı bitti, ana programa dönüldü.")
print_header()                  # aynı gövde ikinci kez çalışır
print("3) Program bitti.")
