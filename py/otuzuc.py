sayilar = list(range(10, 21))

sayilar2 = [21, 22, 23, 24, 25]

birlesik_liste = sayilar + sayilar2

bolunenler = [sayi for sayi in birlesik_liste if sayi % 4 == 0]

print("4'e tam bölünen sayılar:", bolunenler)