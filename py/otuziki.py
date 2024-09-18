def hafta():
    return ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]

gunler = hafta()

indeks = int(input("Bir indeks girin (0-4 arası): "))

if 0 <= indeks < len(gunler):
    print("Girdiğiniz indeksteki gün: "+gunler[indeks])
else:
    print("Geçersiz indeks. Lütfen 0 ile 4 arasında bir değer girin.")
