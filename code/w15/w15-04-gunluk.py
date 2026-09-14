# w15-04-gunluk.py — ekleme ("a") moduyla günlük (log) tutma
from datetime import datetime

LOG_FILE = "gunluk.txt"


def log(message):
    """Mesajı zaman damgasıyla günlüğün SONUNA ekler."""
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{stamp} | {message}\n")


def show_log():
    """Kayıtları numaralayarak listeler (zaman damgası dosyada kalır)."""
    with open(LOG_FILE, encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            stamp, message = line.strip().split(" | ", 1)
            print(f"{number}. {message}")


while True:
    text = input("Kayıt (q = bitir): ")
    if text == "q":
        break
    log(text)
    print("  -> günlüğe eklendi")

print("Günlükteki kayıtlar:")
show_log()
