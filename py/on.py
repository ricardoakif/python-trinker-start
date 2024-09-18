boy = float(input("boyunuzu giriniz: "))
agirlik = float(input("kilonuzu giriniz: "))
vki = agirlik / (boy ** 2)
print(f"Vücut Kitle İndeksiniz: {vki:.2f}")
if vki < 18:
    print("Zayıf")
elif 18 <= vki < 25:
    print("Normal")
elif 25 <= vki < 30:
    print("Fazla kilolu")
else:
    print("Obez")
