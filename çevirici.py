#deger1 = int(input("Bir sayı giriniz: "))
#deger2 = int(input("Lütfen diğer sayıyı giriniz: "))
#toplam = deger1 + deger2
#print(deger1 ,"+",deger2,"=", toplam)

#x = 35
#y = 46
#toplam = x + y
#print(toplam)

dereceF = float (input("Sıcaklığın F derece olarak girin: "))
dereceC = 9/5 * (dereceF - 32)
print(dereceF,"derece F =", dereceC,"C derece")

saniye = int(input("Saniyeyi girin: "))
saat = saniye // 3600
saniye = saniye%3600
dakika = saniye // 60
saniye = saniye % 60
print(saat,"saat", dakika,"dk", saniye, "sn")
#kullanıcı 10000 girerse 2 sa 46 dk 40 sn yazdırı

saniye =int(input("Saate çevrilmesini istediğiniz saniyeyi giriniz: "))
saat = saniye // 3600
saniye = saniye%3600
dakika = saniye // 60
saniye = saniye%60
print(saat,"saat",dakika,"dk",saniye,"sn" )
