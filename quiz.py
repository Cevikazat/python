#print(*"python 3x")  her bir karakterin arasına bir boşluk koyuyor
#print("Ali","Mehmet","Zeynep",sep=",+") ARALARA ARTI ATIYOR
#print(5 if (5<2) else 2) 2 yazar
#print("islem "+("başarili" if (bool(1))else "başarisiz")) işlem başarılı

#1d  2b  3a  4b  5e 6d  7b 8a  9e 10c  11b 12d  13e 14c  15a 16b 17d 18a  19e 20c


#print("python 3x"[::-1]) tersten yzdıır
#print(" %10.4f" %12.34)
#print("{0}{1} ({1}{0})".format("Ali","Kuşçu")) ad soyad (soyadı ad)
#print(sorted("python")) kelimeyi elemanlara ayırır
#print("ali kuşçu".find("k")) girdiğin harfin sırasını söyler
def carp(a,b):
    if(a<b):
        print("ilk opa.")
    print(a*b)