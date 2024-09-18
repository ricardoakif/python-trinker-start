def rakam_topla(sayi):
    toplam = sum(int(rakam) for rakam in str(sayi))
    return toplam

sayi = input("Bir sayı girin: ")

toplam = rakam_topla(sayi)

print("Girdiğiniz sayının rakamlarının toplamı: "+toplam)
