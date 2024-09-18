tercih = input("Sinema mı yoksa tiyatro mu? (S/T): ").upper()
öğrenci = input("Öğrenci misiniz? (E/H): ").upper()

if tercih == "S":
    fiyat = 15
elif tercih == "T":
    fiyat = 10
else:
    print("Geçersiz tercih.")
    exit()

if öğrenci == "E":
    fiyat *= 0.5

print("Ödenecek tutar:"+ fiyat +" TL")
