#liste = []


#for sayi in range(100,1000):
#    toplam = 0
#    gecici_sayi = sayi
#    while gecici_sayi != 0:
#        basamak = gecici_sayi % 10
#        toplam += basamak **3
#        gecici_sayi //= 10
#    if toplam == sayi:
#        liste.append(sayi)
#print(liste)
#print(len(liste))

# 1,1,2,3,5,8,13,21,34,....

#fibonacci_list = []
#fibonacci_list.append(1)
#fibonacci_list.append(2)

#index = 2

#while True:
#    fibonacci_list.append(fibonacci_list[index - 2] + fibonacci_list[index -1])
#    index += 1
#    if len(fibonacci_list) == 100:
#        break
#print(fibonacci_list)
#print(len(fibonacci_list))


#fibonacci_list=list()
#fibonacci_list.append(1)
#fibonacci_list.append(2)

#index = 2

#while True:
#    fibonacci_list.append(fibonacci_list[index -2] + fibonacci_list[index -1])
#    terim = fibonacci_list[index - 1] + fibonacci_list[index - 2]
#    if len(str(terim)) == 1001:
#        print(terim)
#        print(index)
#        break
#    index += 1