# w11-06-kapsam.py — Yerel ve global değişkenler, kapsam ve gölgeleme

MAX_SCORE = 100                 # global (modül düzeyi) ad
count = 0                       # global ad


def percent(score):
    ratio = score / MAX_SCORE   # global ad fonksiyon içinden OKUNABİLİR
    return ratio * 100          # ratio yereldir: fonksiyon bitince silinir


def shadow_demo():
    count = 99                  # aynı adlı YENİ YEREL ad: globali gölgeler
    print("  shadow_demo içinde count =", count)


def increase():
    global count                # "count ile globali kastediyorum" bildirimi
    count = count + 1


print("percent(85) =", percent(85))
shadow_demo()
print("shadow_demo sonrası count =", count)      # 0: global değişmedi
increase()
increase()
print("increase() x2 sonrası count =", count)    # 2: global değişti
