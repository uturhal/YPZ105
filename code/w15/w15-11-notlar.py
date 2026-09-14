# w15-11-notlar.py — kalıcı not dosyası: listele/ekle/güncelle/ortalama
GRADES_FILE = "notlar.txt"


def load_grades():
    """Dosyayı okur; [ad, puan] çiftlerinin listesini döndürür."""
    grades = []
    with open(GRADES_FILE, encoding="utf-8") as f:
        for line in f:
            name, score = line.split()
            grades.append([name, float(score)])
    return grades


def save_grades(grades):
    """Listenin TAMAMINI yeniden yazar ("w" eskisini siler)."""
    with open(GRADES_FILE, "w", encoding="utf-8") as f:
        for name, score in grades:
            f.write(f"{name} {score}\n")


grades = load_grades()               # 1. adım: dosyadan listeye
while True:
    print("1) Listele 2) Ekle 3) Güncelle 4) Ortalama 5) Çık")
    choice = input("Seçim: ")
    if choice == "1":
        for name, score in grades:
            print(f"  {name:<8}{score:>6.1f}")
    elif choice == "2":
        grades.append([input("Ad: "), float(input("Puan: "))])
        save_grades(grades)          # 2-3. adım: değiştir, geri yaz
    elif choice == "3":
        target = input("Kimin notu? ")
        found = [r for r in grades if r[0] == target]
        if found:
            found[0][1] = float(input("Yeni puan: "))
            save_grades(grades)
        else:
            print("  Bulunamadı")
    elif choice == "4":
        total = sum(score for name, score in grades)
        print(f"  Ortalama: {total / len(grades):.2f}")
    elif choice == "5":
        break

print("Dosyanın son hâli:")
with open(GRADES_FILE, encoding="utf-8") as f:
    print(f.read(), end="")
