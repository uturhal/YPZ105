# w14-03-not-cizelgesi.py — 2B çizelge: satır ve sütun ortalamaları

students = ["Ayşe", "Mehmet", "Zeynep", "Can"]
exams = ["Vize", "Final", "Proje"]
grades = [[85, 90, 78],
          [60, 72, 65],
          [95, 88, 100],
          [70, 55, 80]]

header = f"{'Öğrenci':<10}"
for exam in exams:
    header += f"{exam:>7}"
header += f"{'Ort.':>8}"
print(header)
print("-" * len(header))

for i in range(len(students)):              # her satır bir öğrenci
    avg = sum(grades[i]) / len(grades[i])
    line = f"{students[i]:<10}"
    for grade in grades[i]:
        line += f"{grade:>7}"
    print(line + f"{avg:>8.2f}")

print("-" * len(header))
line = f"{'Sınav ort.':<10}"
for j in range(len(exams)):                 # her sütun bir sınav
    col_total = 0
    for i in range(len(students)):
        col_total += grades[i][j]
    line += f"{col_total / len(students):>7.2f}"
print(line)
