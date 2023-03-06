import random

kelimeler = ["berkay","emre","kayseri","sivas","behlül","şeftali","çilek","muz","muş","messi","haaland","çikolata","pişmaniye"]
kelime = "ğ"


def rastgeleKelime():
    global kelime
    kelime = random.choice(kelimeler)
    #print(kelime)
    return kelime.upper()


def oyna(kelime):
    ekran = "_" * len(kelime)
    tahmin = False
    tahminHakkı = 7
    tahminHarf = []
    tahminKelime = []

    print("Kelime oynuna hoşgeldiniz hadi başlayalım!")
    print(ekran)

    while not tahmin and tahminHakkı > 0:
        harf = input("Tahminde bulununuz: ").upper()
        if len(harf) == 1 and harf.isalpha():
            if harf in tahminHarf:
                print("%s harfini daha önce denediniz."%(harf))
            elif harf not in kelime:
                tahminHakkı -=1
                print("%s harfi kelimede yok %d hakkınız kaldı."%(harf,tahminHakkı))
                tahminHarf.append(harf)
            else:
                print("%s harfi kelimede var."%(harf))
                tahminHarf.append(harf)
                dizi = list(ekran)
                index = [i for i,letter in enumerate(kelime) if letter ==harf]
                for ix in index:
                    dizi[ix] = harf
                ekran ="".join(dizi)
                if "_" not in ekran:
                    tahmin = True
            




        elif len(harf) == len(kelime) and harf.isalpha():
            if harf == kelime:
                tahmin = True
                ekran = kelime
            elif harf in tahminKelime:
                print("%s kelimesini daha önce denediniz!"%(harf))
            else:
                print("Cevap doğru değil.")
                tahminKelime.append(harf)
                tahminHakkı-=1


        else:
            print("Geçersiz tahmin yaptınız!")
        print(ekran)
        print("\n")
    if tahmin:
        print("Doğru bildiniz!")
    else:
        print("Maalesef bilemediniz :(\nDoğru cevap: ", kelime)


def başla ():
    kelime = rastgeleKelime()
    oyna(kelime)

başla()
a = input("Tekrar oynamak ister misiniz?(E/H)").upper()
while True:
    if a == "E":
        başla()
        a = input("Tekrar oynamak ister misiniz?(E/H)\n").upper()
    else:
        print("Gülü gülü!")
        break
