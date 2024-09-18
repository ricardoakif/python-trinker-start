def dikdortgen_alani(uzunluk, genislik):
    return uzunluk * genislik

uzunluk = float(input("Dikdörtgenin uzunluğunu girin: "))
genislik = float(input("Dikdörtgenin genişliğini girin: "))
alan = dikdortgen_alani(uzunluk, genislik)
print("Dikdörtgenin alanı:" + alan)
