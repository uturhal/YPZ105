# w14-09-ic-ice-yapilar.py — sözlük listesi ve liste değerli sözlük

students = [
    {"ad": "Ayşe", "no": 2601, "notlar": [85, 90, 78]},
    {"ad": "Mehmet", "no": 2602, "notlar": [60, 72, 65]},
    {"ad": "Zeynep", "no": 2603, "notlar": [95, 88, 100]},
]

for student in students:                # her kayıt bir sözlük
    grades = student["notlar"]
    print(f"{student['no']:<6}{student['ad']:<9}"
          f"{sum(grades) / len(grades):>7.2f}")

for student in students:                # bütün kayıtlara yeni bir alan
    student["durum"] = "geçti" if min(student["notlar"]) >= 60 else "kaldı"
print(students[1])

schedule = {"Pazartesi": ["Matematik", "Fizik"],
            "Salı": ["Programlama"],
            "Çarşamba": []}
schedule["Salı"].append("Lineer Cebir")  # değer bir liste: yerinde ekle

total_lessons = 0
for day, lessons in schedule.items():
    total_lessons += len(lessons)
    text = ", ".join(lessons) if lessons else "(ders yok)"
    print(f"{day:<10}: {text}")
print("Haftalık ders sayısı:", total_lessons)
