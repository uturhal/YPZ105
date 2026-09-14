# YPZ105 — Programlama ve Uygulamaları I

**Trabzon Üniversitesi** · Bilgisayar ve Bilişim Fakültesi · **Yapay Zeka Mühendisliği Bölümü**
1. sınıf, güz yarıyılı · 3 saat teori + 1 saat uygulama (haftada 4 saat, tamamı laboratuvarda) · 4 AKTS
Öğretim elemanı: **Dr. Öğr. Üyesi Uğur Turhal**

Bu depo dersin **ders notunu** ve **kitaptaki bütün örnek programları** barındırır. Kitaptaki her
kod kutusunun sağ üstündeki karekod, o dosyanın buradaki kopyasına gider — telefonunuzla okutup
kodu tarayıcıda açabilir ya da indirebilirsiniz.

---

## 📘 Ders notu

**[YPZ105-Ders-Notu.pdf](YPZ105-Ders-Notu.pdf)** · 362 sayfa · en son 14 Eylül 2026

Kitap dersin resmî müfredatını hafta hafta izler; her bölüm, dört saatlik **tek bir laboratuvar
oturumunda** anlatılıp uygulanacak kadar malzeme içerir — ne daha azı, ne daha fazlası.

| Hafta | Konu | Neler var |
|:---:|---|---|
| 1 | Bilgisayarda temel kavramlar | von Neumann mimarisi, bellek hiyerarşisi, sayı sistemleri (ikili/onluk/onaltılık), verinin gösterimi (tam sayı taşması, ASCII/Unicode, piksel/RGB, ses), yazılım katmanları, YZ boru hattı |
| 2 | Algoritma ve akış diyagramları I | problem çözme süreci, algoritmanın beş özelliği, sözde kod sözleşmesi, ISO 5807 sembolleri, izleme tablosu, sıralı algoritmalar |
| 3 | Algoritma ve akış diyagramları II | karar ve tekrar yapıları, karar tablosu, doğruluk tabloları, biriktiriciler, klasik algoritmalar (faktöriyel, asal, EBOB), arama ve adım sayısı sezgisi |
| 4 | Python'a giriş | yorumlayıcı/derleyici, IDLE–PyCharm–Colab, değişken ve atama, `int`/`float`/`str`/`bool`, tür dönüşümü, `input`/`print`, operatörler ve öncelik, f-string, hata mesajını okumak |
| 5 | Karakter dizisi (string) işlemleri | indeksleme, dilimleme, değiştirilemezlik, `upper`/`strip`/`replace`/`split`/`join` ve arkadaşları, Unicode ve Türkçe `i`/`İ` sorunu, hizalama |
| 6 | Koşullu ifadeler I | karşılaştırma operatörleri, girinti ve blok kuralı, `if`/`elif`/`else`, `and`/`or`/`not`, kısa devre, doğruluk değeri olan nesneler, `float` karşılaştırma tuzağı |
| 7 | Koşullu ifadeler II | iç içe koşullar, karar tablosundan koda, De Morgan ile sadeleştirme, `match-case`, girdi doğrulama, sınır durumları, menü programları |
| 8 | `while` döngüsü | koşul–gövde–güncelleme, sayaç ve biriktiriciler, nöbetçi değer, `break`/`continue`, sonsuz döngü ve birim kayması, sayı tahmin oyunu |
| **9** | **Ara sınav (vize)** | kapsam, sınav biçimi, hazırlık önerileri |
| 10 | `for` döngüsü ve seriler | `range`, metin üzerinde döngü, iç içe döngüler ve desenler, `enumerate`/`zip`, seri toplamlarıyla yaklaşım, adım sayısı ve verimlilik sezgisi |
| 11 | Fonksiyonlar I | `def`, parametre ve argüman, `return` ile `print` farkı, kapsam (scope), docstring, yukarıdan aşağıya tasarım, `main()` düzeni |
| 12 | Fonksiyonlar II | varsayılan ve anahtar sözcüklü argümanlar, çoklu dönüş, `*args`, özyineleme ve çağrı ağacı, `lambda`, kendi modülünü yazmak, `assert` ile test |
| 13 | Tek boyutlu listeler | liste metotları, dilimleme, takma ad ve kopyalama, liste üreteci, arama ve sıralama algoritmaları, istatistikler |
| 14 | İki boyutlu listeler, demet, sözlük | matris işlemleri ve görüntü benzetmesi, demet ve çoklu dönüş, sözlük (CRUD, frekans sayma), küme, hangi yapı ne zaman |
| 15 | Metin dosyası yönetimi | `open` modları ve `with`, satır satır okuma, CSV, `try–except`, kayıt güncelleme deseni, JSON'a bakış, kodlama ve Türkçe karakterler |
| **16** | **Final sınavı** | kapsam, ağırlık dağılımı, hazırlık önerileri |

**Kitabın içinde:** 108 şekil · 73 çözümlü örnek · 165 alıştırma (**hepsinin cevabı var**) ·
124 numaralı kod kutusu · 14 laboratuvar çalışması · Ek B kurulum kılavuzu ·
Ek C Python hızlı başvuru (sınav öncesi tek oturuşta gözden geçirilecek tablolar) ·
Ek F cevaplar · dizin.

### Kutular ne anlama gelir?

| | |
|---|---|
| 🟥 **Tanım** | Yeni bir kavramın kesin tanımı. Numaralıdır (Tanım 4.2), metinden gönderme yapılır. |
| 🟦 **Kural** | Dilin ya da algoritma tasarımının her zaman geçerli kuralı. Kırıldığında program çalışmaz ya da yanlış çalışır. |
| 🟩 **Örnek + Çözüm** | Her çözüm aynı iskelettedir: **Analiz → Algoritma → Kod ve çıktı → Kontrol**. Kontrol adımı isteğe bağlı değildir. |
| 🔵 **İpucu** | Kısayol, daha okunur yazım, pratik bilgi. |
| 🟠 **Dikkat** | Sonucu sessizce yanlış çıkaran tuzak. |
| 🔴 **Sık yapılan hata** | Gerçekten puan kaybettiren hatalar; yanlış ve doğru yan yana gösterilir. |
| 🟦 **Laboratuvar** | O haftanın ders içi görevleri, beklenen çıktılarıyla birlikte. |

Ayrıntılı açıklama kitabın **"Başlarken"** bölümündedir; ilk haftadan önce okumanız önerilir.

---

## 💻 Örnek kodlar

[`code/`](code) klasöründe, haftalara göre ayrılmış **127 program**:

```
code/w04/w04-01-merhaba.py        ← kitaptaki Kod 4.1
code/w04/w04-04-donusum.in        ← programın beklediği klavye girdisi (varsa)
code/w04/out/w04-01-merhaba.out   ← programın gerçekten ürettiği çıktı
```

Kitapta basılı olan çıktı, `out/` klasöründeki dosyadan gelir: kitabın her sürümünde bütün
programlar otomatik olarak çalıştırılır ve çıktıları yeniden üretilir. Yani **kitapta gördüğünüz
çıktı ile dosyanın gerçek çıktısı birbirinden farklı olamaz.**

İlk üç haftanın klasörü yoktur: o haftalarda henüz Python yazmıyoruz, algoritmaları sözde kod ve
akış diyagramıyla tasarlıyoruz.

### Bir programı çalıştırmak

```bash
cd code/w04
python w04-01-merhaba.py
```

`.in` dosyası olan programlar klavyeden veri bekler; o dosyadaki satırlar, sırayla girmeniz
gereken değerlerdir. Örneğin `w04-04-donusum.in` içinde `19` ve `1.75` yazıyorsa, program
çalışınca önce `19`, sonra `1.75` yazıp Enter'a basın.

15\. haftanın bazı programları **veri dosyası** okur (`notlar.txt`, `ogrenciler.csv`); bu
dosyalar da aynı klasördedir, programla birlikte indirmeniz yeter.

### Tümünü indirmek

Yukarıdaki yeşil **Code** düğmesi → **Download ZIP**. Ya da git kullanıyorsanız:

```bash
git clone https://github.com/uturhal/YPZ105.git
```

---

## 🛠 Çalışma ortamı

Ders **Python 3.10 veya üstünü** kullanır. Kurulum adımları — Anaconda, IDLE, PyCharm Community
ve Google Colab için ayrı ayrı, sık karşılaşılan sorunların çözümleriyle birlikte — ders notunun
**Ek B**'sindedir.

Kendi bilgisayarınıza kurulum yapamıyorsanız [Google Colab](https://colab.research.google.com)
tarayıcıda çalışır ve hiçbir şey kurmanızı gerektirmez; ders boyunca geçerli bir seçenektir.

Örnek programlar yalnız **standart kütüphaneyi** kullanır (`math`, `random`, `csv`, `json`,
`os`, `statistics`); ek paket kurmanıza gerek yoktur.

---

## 📊 Değerlendirme

| Bileşen | Adet | Birim ağırlık | Toplam | Haftalar |
|---|:---:|:---:|:---:|---|
| Kısa sınav | 5 | %5 | %25 | 3, 6, 8, 12, 15 |
| Ara sınav (vize) | 1 | %25 | %25 | 9 |
| Final | 1 | %50 | %50 | 16 |

Başarı notu = 0,05 × (beş kısa sınavın toplamı) + 0,25 × vize + 0,50 × final.

**Ödev ve proje yoktur.** Laboratuvar görevleri ders içinde yapılır ve notlandırılmaz — ancak
kısa sınav ve vize sorularının önemli bir kısmı doğrudan o görevlerden türetilir.

Kısa sınavlar ilgili haftanın dersinin **son 25 dakikasında**, laboratuvarda, kâğıt üzerinde
yapılır; ayrı bir sınav saati ilan edilmez. Sınav tarihlerinin tamamı ve her sınavın kapsamı ders
notunun **Ek A**'sındadır. Devam, mazeret ve bütünleme konularında üniversitenin ilgili
yönetmeliği esastır.

---

## 🐛 Hata bildirimi

Notlar yeni yazıldı ve hata içerebilir. Bir yanlış bulursanız — yazım, hesap, çalışmayan kod,
bozuk karekod — **Issues** sekmesinden bildirin. Sayfa numarasını ya da dosya adını yazmanız
yeter; düzeltilenler bir sonraki sürüme girer.

Kitaptaki her sayı bağımsız olarak yeniden hesaplanarak denetlenir (şu an 1680 otomatik kontrol)
ve her program çalıştırılarak çıktısı doğrulanır; yine de gözden kaçanlar olabilir.

---

## 📄 Lisans

| İçerik | Lisans |
|---|---|
| Ders notu (`YPZ105-Ders-Notu.pdf`) | [CC BY-NC-SA 4.0](LICENSE-NOTES) — kaynak göstererek, ticari olmayan amaçla paylaşabilir ve uyarlayabilirsiniz |
| Kaynak kodlar (`code/`) | [MIT](LICENSE) — serbestçe kullanabilirsiniz |

Kitaptaki metin, şekil ve örneklerin tamamı bu ders için özgün olarak hazırlanmıştır; hiçbir
kaynaktan alıntılanmamıştır. Yararlanılan kaynaklar konu kapsamı için ders bilgi paketinde
listelenmiştir.
