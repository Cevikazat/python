kişi = {"İsim":"heval","Yaş":20,"okul":"uludağ.üni","hobiler":["kitap okuma","şiir yazma","sinema"]}

print(kişi["İsim"])
kişi.update({"İsim":"azat","Yaş":22})# birden fazla alanda değişiklik sağlar
kişi["İsim"]= "azat"
kişi["id"]= 12345# id ekleme yapar
print(kişi)
del kişi["id"] #del siler ing delete
print(kişi)
for x in kişi:
    print(x)   #anahtarları yazdırır
for x in kişi:
    print(kişi[x]) # values yazdırır

kişi = {"İsim":"heval","Yaş":20,"okul":"uludağ.üni","hobiler":["kitap okuma","şiir yazma","sinema"]}

print(kişi.values()) #keys anahtar  values cevap
print(kişi.items()) #together writing
for k,v in kişi.items():
    print(k,v)  #anahtar ve cevap birlikte yazdırır
print(kişi.get("id"))#  varsa değer döndürür yoksa hata vermez değer yok der

