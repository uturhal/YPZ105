# w15-10-hata.py — dosya hatalarını yakalama: try / except / else / finally
import os


def read_first_line(filename):
    """Dosyanın ilk satırını döndürür; sorun varsa None döndürür."""
    try:
        with open(filename, encoding="utf-8") as f:
            first = f.readline().strip()
    except FileNotFoundError:
        print(f"  HATA: '{filename}' bulunamadı.")
        first = None
    except PermissionError:
        print(f"  HATA: '{filename}' için okuma izni yok.")
        first = None
    else:                            # yalnız hata ÇIKMADIYSA
        print(f"  Okundu: {first}")
    finally:                         # her durumda, en son
        print(f"  ({filename} denemesi bitti)")
    return first


for name in ["siir.txt", "yok.txt"]:
    print(f"{name}:")
    result = read_first_line(name)
    print("  dönen değer:", repr(result))

# Açmayı denemeden önce sormak: os.path.exists
print("notlar.txt var mı?", os.path.exists("notlar.txt"))
print("yok.txt var mı?   ", os.path.exists("yok.txt"))
