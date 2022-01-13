#ekrandan alınan bir sayının faktöryelini hesaplayan bir program yazınız

sayı =int(input("Bir sayı girniz"))

prime = True

for i in range(2,sayı):
    if sayı %i == 0:
        prime = False
        break
if prime == True:
    print(f"{sayı} sayısı asaldır")
else:
    print(f"{sayı} sayısı asal değildir")

sayı = int(input("Bir sayı giriniz: "))

bölen_sayısı = 0

for i in range(1,sayı +1):
    if sayı %i == 0:
        bölen_sayısı += 1
print(f"{sayı} sayısının {bölen_sayısı} tane böleni vardır")

sayı = int(input("Bir sayı giriniz"))

str_sayı = str(sayı)
toplam = 0
for rakam in str_sayı:
    toplam += int(rakam)
print(toplam)
toplam = 0
geçici_sayı = sayı
while geçici_sayı != 0:
    basamak = geçici_sayı % 10
    toplam += basamak
    geçici_sayı//=10

print(toplam)


sayı = int(input("Bir sayı girniz: "))
faktöriyel = 1
i =2
while i <= sayı:
  faktöriyel *= i
  i += 1

print(f"{sayı} ! = {faktöriyel}")
sayi = int(input("Bir sayı giriniz: "))
prime = True
for i in range(2,sayi):
  if sayi %i == 0:
    prime=False
    break
if prime == True :
  print(f"{sayi} sayısı asaldır")
else:
  print(f"{sayi} sayısı asal değildir")
sayi = int(input("Bir sayı giriniz: "))

bolen_sayisi = 0
for i in range(1,sayi + 1):
  if sayi %i == 0:
    bolen_sayisi += 1
print(f"{sayi} sayısının {bolen_sayisi } tane böleni var.")
sayi = int(input("Bir sayı giriniz: "))
str_sayi = str(sayi)
toplam = 0
for rakam in str_sayi:
  toplam += rakam
print(toplam)

sayi= int(input("Bir sayı giriniz: "))
str_sayi = str(sayi)
toplam = 0
for rakam in str_sayi:
  toplam += int(rakam)
print(toplam)

sayi= int(input("Bir sayı giriniz: "))
toplam = 0
gecici_sayi = sayi
while gecici_sayi !=0:
  basamak = gecici_sayi % 10
  toplam += basamak
  gecici_sayi//=10

print(toplam)

b = []
for i in range(7):
  a = int(input("Bir sayı giriniz: "))
  b.append(a)
print(f"en büyük sayı: {max(b)}")
print(f"en küçük sayı :{min(b)}")

b = int(input("Bir sayı giriniz: "))
karekok =b**0.5
if karekok == int(karekok):
  print("Tam kare")
else:
  print("Tam kare değil")


metin = input("Bir metin giriniz: ")
sozluk= dict()
for harf in metin:
  if harf in sozluk:
    sozluk[harf] +=1
  else:
      sozluk[harf] = 1
for harf,adet in sozluk.items():
  print(harf,adet)

metin = input("Bir metin giriniz: ")
metin2 = ""
for harf in metin:
  if harf == "n":
    metin2 += "N"
  else:
    metin2 += harf
print(metin2)