def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False
    return True

sayi = int(input("sayı gir: "))
if asal_mi(sayi):
    print(sayi+ "asal sayı")
else:
    print(sayi+ "asal sayı değil.")
