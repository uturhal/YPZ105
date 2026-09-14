# w07-12-chatbot.py — Evet/hayır sorularıyla karar ağacı: destek "chatbot"u

print("Destek botuna hoş geldiniz. Sorulara e (evet) / h (hayır) yazın.")
a1 = input("Bilgisayarınız açılıyor mu? ").strip().lower()

if a1 == "e":
    a2 = input("Ekranda görüntü var mı? ").strip().lower()
    if a2 == "e":
        a3 = input("İnternete bağlanabiliyor musunuz? ").strip().lower()
        if a3 == "e":
            print("Öneri: Sorunu ayrıntılı yazın, teknisyene aktarıyorum.")
        else:
            print("Öneri: Modemi 30 saniye kapatıp yeniden açın.")
    else:
        print("Öneri: Monitör kablosunu ve parlaklık ayarını kontrol edin.")
elif a1 == "h":
    a2 = input("Güç kablosu prize takılı mı? ").strip().lower()
    if a2 == "e":
        print("Öneri: Güç düğmesine 10 s basılı tutun; olmazsa servise.")
    else:
        print("Öneri: Kabloyu takın ve yeniden deneyin.")
else:
    print(f"'{a1}' anlaşılmadı; yalnız e ya da h yazın.")
