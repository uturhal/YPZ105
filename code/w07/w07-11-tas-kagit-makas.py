# w07-11-tas-kagit-makas.py — Taş-kâğıt-makas (tek el): random.choice
import random

OPTIONS = "TKM"                      # T: taş, K: kâğıt, M: makas
computer = random.choice(OPTIONS)    # metinden rastgele bir karakter
user = input("Seçiminiz (T/K/M): ").strip().upper()

if len(user) != 1 or user not in OPTIONS:
    print(f"Geçersiz seçim: '{user}'. T, K ya da M girin.")
else:
    print(f"Siz: {user}   Bilgisayar: {computer}")
    if user == computer:
        print("Berabere!")
    elif ((user == "T" and computer == "M")
          or (user == "K" and computer == "T")
          or (user == "M" and computer == "K")):
        print("Kazandınız!")
    else:
        print("Bilgisayar kazandı.")
