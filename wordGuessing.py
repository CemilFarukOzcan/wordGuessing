import random

kelimeler = [
"worm","suspicion","carpet"
"news","real","range"
"shadow","hip","athlete"
"abstract","terrace","waist"
"lead","underline","consider"
]

kelime = random.choice(kelimeler)
print("karakterleri tahmin et!")

tahminler = " "

tur= 12

while tur > 0 :
    hata = 0

    for karakter in kelime:
        if karakter in tahminler:
            print(karakter, end=" ") 
        else:
            print("_")
            hata += 1
    
    if hata == 0:
        print("tebrikler kelimeyi buldunuz")
        print("kelime: ",kelime)
        break


    print()
    tahmin = input("karakter tahmin et: ")

    tahminler += tahmin

    if tahmin not in kelime:
        tur -= 1
        print("yalnis")
        print(tur , "hakkin kaldi")
    if tur == 0:
        print("kaybettin")
        print("kelime: ",kelime)
