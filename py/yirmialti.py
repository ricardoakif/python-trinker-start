import random

def sayi_tahmin_oyunu():
    hedef_sayi = random.randint(1, 100)
    hak = 3
    
    print("1 ile 100 arasında bir sayı tahmin edin! 3 hakkınız var.")
    
    while hak > 0:
        tahmin = int(input("Tahmininiz: "))
        if tahmin == hedef_sayi:
            print("dogru tahmin!")
            break
        elif tahmin < hedef_sayi:
            print("Daha büyük bul.")
        else:
            print("Daha küçük bul.")
        
        hak -= 1
        print(f"Kalan hakkınız: {hak}")
        
    if hak == 0:
        print(f"Maalesef, kaybettiniz! Doğru sayı {hedef_sayi} idi.")

sayi_tahmin_oyunu()