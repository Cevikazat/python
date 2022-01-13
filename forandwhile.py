#liste = [1,2,3,4,5,6]
#for rakam in liste:
#    print(rakam)

#isim= "Azat"
#for harf in isim:
#    print(harf)

#a = (1,2,3,4,5,6)
#for i in a:
#    print(i)
# range aralık yazdırır
#sonuc = 3
#for i in range(0,9):
#    sonuc *= 2
#print(sonuc)

#liste1 = ["a","b","c"]
#liste2 = [1,2,3,]
#for i in liste1:
#    for d in liste2:
#        print(i,d)
#liste = [1,2,3,4,5,6,7,8,9]
#for i in liste:
 #   if i == 3:
  #      print("3'ü atladık")
   #     continue
    #print(i)

#liste = range(101)

#for i in liste:
#    if i % 3 != 0:
#        continue
#    print(i)
#x = 5
#while x < 20: koşul sağlandıkça devam eder 
#    print(x)
#    x +=3 artış miktarı 3

#i = 5
#while True:
#    print(i)
#    i +=5
#    if i ==2000:
#        break

#i = 3
#while True:
#    if i %2 ==0:
#        i += 1
#        continue
#    print(i)
#    i += 1
#    if i == 1000:
#        break


prime_list=list()

prime_list.append(2)
sayi=3
while True:
    prime = True
    for i in range(2,int(sayi**0.5) + 1):
        if sayi %i ==0:
            prime = False
    if prime:
        prime_list.append(sayi)
        if len(prime_list) == 1000:
            break
    sayi += 1
print(prime_list)

liste2 = []
for prime in prime_list:
    strprime=str(prime)
    if strprime.startswith("3") and strprime.endswith("7"):
        liste2.append(prime)
print(liste2)
print(len(liste2))
