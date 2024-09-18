import random

def besin_katlari(liste):
    besin_katlari = [sayi for sayi in liste if sayi % 5 == 0]
    return besin_katlari

liste = [random.randint(1, 100) for a in range(10)]

sonuc = besin_katlari(liste)
print("Liste içindeki 5'in katları:", sonuc)
