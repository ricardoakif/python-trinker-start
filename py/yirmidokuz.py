def kontroletme(metin, karakter):
    if karakter in metin:
        return True
    else:
        return False

metin = input("Bir metin girin: ")
karakter = input("Kontrol etmek istediğiniz karakteri girin: ")

if(kontroletme(metin,karakter)==True):
    print(karakter+" karakteri metinde bulunuyor.")
else:
    print(karakter+" karakteri metinde bulunmuyor.")
