import math

def daire_alani(yaricap):
    return math.pi * (yaricap ** 2)

yaricap = float(input("Dairenin yarıçapını girin: "))
alan = daire_alani(yaricap)
print(f"Dairenin alanı:"+alan)
