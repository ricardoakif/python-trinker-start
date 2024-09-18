def ciftmi(sayi):
    return sayi % 2 == 0

def ciftort(s1, s2):
    ciftsayilar = [sayi for sayi in range(s1, s2 + 1) if ciftmi(sayi)]
    if ciftsayilar:
        return sum(ciftsayilar) / len(ciftsayilar)
    else:
        return None

s1 = int(input("Birinci sayıyı girin: "))
s2 = int(input("İkinci sayıyı girin: "))

ortalama = ciftort(s1, s2)

if ortalama is not None:
    print(f"{s1} ile {s2} arasındaki çift sayıların ortalaması: {ortalama}")
else:
    print("Bu aralıkta hiç çift sayı yok.")
