tek = 0
cift = 0
sayi = int(input("Bir sayı girin: "))

for i in range(1, sayi + 1):
    if i % 2 == 0:
        cift += i
    else:
        tek += i

print("Tek sayıların toplamı:"+ tek +"Çift sayıların toplamı:"+ cift)
