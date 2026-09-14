# w15-12-json-ayarlar.py — bir sözlüğü JSON dosyasına yazma ve geri okuma
import json

settings = {
    "kullanici": "Ayşe",
    "yazi_boyutu": 14,
    "bildirimler": True,
    "son_dosyalar": ["notlar.txt"],
}

with open("ayarlar.json", "w", encoding="utf-8") as f:
    json.dump(settings, f, indent=2, ensure_ascii=False)

# JSON dosyası düz metindir; içine bakalım
with open("ayarlar.json", encoding="utf-8") as f:
    print(f.read())

# Geri yükleme: türler korunur (int, bool, list)
with open("ayarlar.json", encoding="utf-8") as f:
    loaded = json.load(f)

print(type(loaded), loaded == settings)
print(loaded["yazi_boyutu"] + 2, type(loaded["bildirimler"]))
