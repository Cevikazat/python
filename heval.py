#print('Ali\'nin Evi')
#print("Merhaba \n Dünya")

#mesaj="Merhaba Dünya"

#print(mesaj)

#mesaj="Merhaba"

#mesaj2="Dünya"

#print(mesaj +" "+ mesaj2)
#print(mesaj[0:4])
#print(mesaj[::-1])
#print(mesaj.upper())
#mesaj = mesaj.upper()
#print(mesaj)
#mesaj = mesaj.lower()
#print(mesaj)
#mesaj = mesaj.capitalize()
#print(mesaj)
#print(mesaj.startswith("Me"))
#print(mesaj.endswith("a"))
#print("Merhaba" + " " + mesaj2)
#print("Merhaba"*6)
#isim = "Heval"
#yaş ="20"
#üni ="uludağ "
#print("{}  {} yaşındadır {} üniversitesine okuyor ".format(isim,yaş,üni))
#mesaj = "fuck of"
#print(" {} {} dedi...".format(isim,mesaj)) 
#print(f"{isim} {mesaj} dedi")

#integr = tam sayı float= ondalık sayı
#type= float veya integr olduğunu gösterir

#sayı1 = 5**3
#sayı2 = 23/4
#print(type(sayı1))
#print(sayı2)
#print(41//4)
#print(5**3)
#print(abs(-2.13)) integr ve float olabilir
#sayı = 22/7
#print(round(sayı)) yuvarlama
#print(round(sayı,2))
#print(3*7+9) işlem önceliği
#print((3+5) * 4+9)
#karşılaştırma operatörleri
#print(3==3) eşiitir 
#sayı1 = 7
#sayı2=10
#sayı3=10
#print(sayı2 <= sayı3)
#sayı1 = "100"
#sayı2 = 100
#sayı3 = int(sayı1)
#print(type(sayı1))
#print(type(sayı2))
#print(sayı1==sayı2)
#print(sayı3==sayı2)
#sayı3 = abs(-4.45) abs mutlak değer fonk.
#sayı = 123
#sayı2 = str(sayı)
#print(type(sayı2))

#i = 1
#i *= 5
#i /= 5
#print(i)

# listeler
#renkler= ["siyah","Beyaz","sarı","Mavi","Yeşil"]
#renkler.append("Gri") ekleme 
#renkler2 = ["Turuncu","Pembe"]
#renkler.extend(renkler2) ekleme 
#.pop silme fonk
#silinen = renkler.pop()  silineni gösterir

#renkler= ["Siyah","Beyaz","sarı","Mavi","Yeşil"]
#sayılar = [1,2,39,4,3,7,8]
#print(min(sayılar))
#print(max(sayılar))
#print(sum(sayılar)) toplar *
#for renk in renkler:
 #   print(renk)
#print(list(enumerate(renkler,start=2)))
#print("Siyah" in renkler)
#stringrenkler = "-".join(renkler) ekleme 
#print(stringrenkler)

#renkler2 = stringrenkler.split("Ma") parçalama 
#print(renkler2),

#küme= {"Sarı","Mavi","Yeşil","Kırmızı","Siyah"}
#for renk in demet:
#    print(renk)
#küme1= {"Sarı","Mavi","Yeşil","Kırmızı","Siyah"}
#küme.discard("Siyah")
#küme2 = {"Sarı","Mavi","Yeşil","Beyaz","Gri"}
# difference fark       union birleşim  intersection kesişim
#print("Beyaz" in küme1.union(küme2))
#bosliste1= []
#bosliste2 = list()

#bosdemet1=()
#bosdemet2 = tuple()

#boskume1= set()
#boskume2 ={} #bu bir sözlüktür
#python = set("1,2,3,4,5,6")
#print(python)

#heval=list("HEVAL")
#print(list(heval))

#çiçek = tuple("ÇİÇEK")
#print(tuple(çiçek))

#book = "kitap"
#cat = "kedi"
#car = "araba"
#love = "aşk"

#kisi = {"isim" : "azat", "yaş" : "20" , "cinsiyet" : "erkek" ,"hobiler" : ["sinema","kitap okuma","boş yapma"]}

#kisi["id"] = 12345
#print(kisi)
#del kisi["id"]
#for x in kisi:
 #   print(kisi[x])
#print(kisi.keys()) anahtar kelimeleri yazdırır
#print(kisi.values()) değerlerri yazdırır
#print(kisi.items()) birlikte yazdırır
#for k,v in kisi.items():
    #print(k,v) birlikte yazdırır 

#print(kisi.get("takma ad", "bulunamadı"))
