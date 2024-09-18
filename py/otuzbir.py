def dikdortgen_alani(genislik, yukseklik):
    return genislik * yukseklik

genislik = float(input("Dikdörtgenin genişliğini girin: "))
yukseklik = float(input("Dikdörtgenin yüksekliğini girin: "))

alan = dikdortgen_alani(genislik, yukseklik)

print("Dikdörtgenin alanı: "+alan)
