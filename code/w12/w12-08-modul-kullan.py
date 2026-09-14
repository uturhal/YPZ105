# w12-08-modul-kullan.py — Kendi modüllerimizi kullanan ana program
import w12geometry as geometry            # modülün tamamı, takma adla
from w12caesar import encrypt, decrypt    # yalnız iki ad alınır

r = float(input("Yarıçap (cm): "))
print(f"Alan : {geometry.circle_area(r):.2f} cm²")
print(f"Çevre: {geometry.circle_perimeter(r):.2f} cm")

# from ... import ... ile gelen adlar modül adı yazılmadan kullanılır
secret = encrypt("Trabzon 2026", 5)
print("Şifreli:", secret, "| Çözülen:", decrypt(secret, 5))
print("Modülün adı:", geometry.__name__, "| Bu dosya:", __name__)
