from datetime import datetime

def yil_gunu_hesapla(tarih):
    tarih_objesi = datetime.strptime(tarih, '%Y-%m-%d')
    return tarih_objesi.timetuple().tm_yday

tarih = input("Tarihi girin (YYYY-MM-DD formatında): ")
gun = yil_gunu_hesapla(tarih)
print(f"{tarih} tarihi yılın {gun}. günü.")
