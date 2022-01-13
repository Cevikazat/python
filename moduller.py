

#import benim_matematik_modulum 

#sonuc = benim_matematik_modulum.daire_alan(6)
#print(sonuc)

#from benim_matematik_modulum import cember_cevresi

#sonuc = cember_cevresi(5)
#print(sonuc)

#import benim_matematik_modulum (as bnm)> ismin yerine kullanılır
#sonuc = bnm.daire_alan(3)
#print(sonuc)

# random 0 ile 10 arasındaki sayılar ile ondalıklı sayılar oluşturyor  and uniform sınır belirieyip ondalıklı sayılar yazdırıyor

#import random 

#for i in range(10):
#    print(random.uniform(10,23))
#    print(random.randint(1,13))
#   print(random.randrange(1,10,3))

# choice rastgele seçer
#liste = ["Siyah", "Beyaz", "Mavi", "Yeşil", "Gri", "Turuncu"]
#print(random.choice(liste)) rastgele yazdırır

# shuffle karıştırır
#random.shuffle(liste)
#print(liste)

# sample eleman sayısı ve liste alıyor istediğiniz kadar rASTGELE ELEMAN SEÇER
#print(random.sample(liste,3))

# zar olasılık hesaplama 

#zarlar = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

#for i in range(100):
#    zar = random.randint(1,6)
#    zarlar [zar] += 1

#for zar in zarlar :
#    print(f"{zar} gelme olasılığı: {zarlar[zar] / 100} ") 
#
# 6-6 gelmesi için atılması gereken sayı
#alt_alt = 0
#dnm_says = 0
#while True:
#    dnm_says += 1
#    zar1 = random.randint(1,6)
#    zar2 = random.randint(1,6)
#    if zar1 == 6 and zar2 ==6:
#        alt_alt += 1
#    if alt_alt == 10:
#        print(f"10 kere 6-6 gelmesi için zarlar {dnm_says} atılmalıdır") 
#        break
#import time

#zaman = time.time()
#print(zaman)    başlangıç zamanı 1970 alınarak bu güne kadar geçen zamanın saniye cinsinden değerini yzdırır.

#baslangic = time.time()
#liste =  []
#for i in range(1000000):
#    liste.append(i)
#bitis = time.time()
#print(bitis - baslangic)

#zaman = time.ctime()
#print(zaman)      bugünün tarihini veriyor / değr girilirse başlangıçtan girilen değer kadar sre geçer ve tarih bulunur.

#zaman = time.localtime()
#print(zaman)  ayrıntılın yzdırır

#zaman = time.asctime() 
#print(zaman)  

#zaman = time.strftime("%d:%m:%Y - %H:%M:%S") istediğin düzende yazdırır
#print(zaman)

#print("Program başlatıldı")
#time.sleep(5)
#print("Program sonlandı")

#from datetime import date, datetime

#bugun = date.today()
#print(bugun)

#gecmis_tarih = date(2015,9,17)
#print(gecmis_tarih)

#gecen_zaman = bugun - gecmis_tarih
#print(gecen_zaman)

#suan = datetime.now()

#print(suan)
#print(suan.ctime())
#print(datetime.ctime(suan))

#import os 

#print(os.getcwd)
#os.chdir("/Users/cevik/python")

#print(os.listdir("/Users/cevik/python"))
#for dosya in os.listdir():
#    print(dosya)

#os.mkdir("Denemeklasörü")  klasör oluşturur

#os.makedirs("Deneme1/Deneme2/Deneme3") # iç içe dosya oluşturur 

#os.rmdir("Deneme1")  dosya siler 

#os.removedirs("Deneme1/Deneme2/Deneme3")  # içteki boş dosyayı siler

