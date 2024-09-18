def hesapla():
    toplam = 0
    
    while True:
        sayi = float(input("Bir sayı girin : "))
        toplam += sayi
        toplamstring = str(toplam)
        if sayi == 0:
            break
        
    print("Girilen sayıların toplamı: "+toplamstring)

hesapla()
