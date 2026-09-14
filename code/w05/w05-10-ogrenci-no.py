# w05-10-ogrenci-no.py — Öğrenci numarasını denetleme ve parçalama
# Biçim: YYYYBBBSSS — 4 hane yıl, 3 hane bölüm, 3 hane sıra no

student_no = input("Öğrenci numarası: ").strip()

year = student_no[:4]
dept_code = student_no[4:7]
order = student_no[7:]

print("Uzunluk 10 hane   :", len(student_no) == 10)
print("Yalnız rakam      :", student_no.isdigit())
print("Bu yıl kayıtlı    :", student_no.startswith("2026"))
print("YZ Müh. (105)     :", dept_code == "105")
print()
print("Giriş yılı :", year)
print("Bölüm kodu :", dept_code)
print("Sıra no    :", order, "->", int(order))
