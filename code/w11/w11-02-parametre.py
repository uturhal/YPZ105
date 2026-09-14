# w11-02-parametre.py — Parametreli fonksiyonlar: print_line, draw_triangle

def print_line(ch, n):
    """ch karakterini n kez yan yana yazar."""
    print(ch * n)


def draw_triangle(n):
    """n satırlık yıldız üçgeni çizer."""
    for i in range(1, n + 1):
        print("*" * i)


print_line("-", 20)             # ch = "-", n = 20
print_line("*", 5)              # aynı gövde, başka argümanlar
print()
draw_triangle(4)                # n = 4
