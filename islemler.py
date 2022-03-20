#Hazırlanan uygulama Z8 Grubunun toplama işleminin mod 8 hesabına göre çalışır.
from copy import copy
from kombinasyonlar import tum_kombinasyonlar

ugh_saglar = list()
ugh_saglamaz = list()

def incele(kume1,kume2):
    #Verilen iki küme arasında fonksiyonu tanımlamak amacıyla yazıldı.
    #Parametre olarak iki tane 4 elemanlı küme alacak.
    fonksiyon = dict()
    for i in range(0,len(kume1)):
        fonksiyon[kume1[i]] = kume2[i]
        #Sözlük fonksiyon gibi çalışıp değerleri key ve value olarak eşleyecek.
    print(fonksiyon)
    return fonksiyon
    # Buraya kadar çalışıyor

def ikili_kombinasyonlar(kume):
    #Bu fonksiyon ile ilk kümenin ikili kombinasyonlarını aldık.
    ikili_kombinasyonlar_ = list()
    liste_ = list()
    for i in range(0,len(kume)):
        if(len(kume)>=2):
            x = kume[0]
            kume.remove(kume[0])
            for j in range(0,len(kume)):
                y = kume[j]
                liste_.append(x)
                liste_.append(y)
                ikili_kombinasyonlar_.append(liste_)
                liste_ = []
    return(ikili_kombinasyonlar_)


def islem(kume1,kume2):
    #Bellekte gösterilen alandan diğer kümeyi ayırmak için kopyasını aldım.
    kume1_ = copy(kume1)
    #Buraya gelen x ve y değerleri kume1 içerisinde olmak zorunda aksi takdirde hata verir.
    #f([x,y])=[f(x),f(y)]
    #Önce iki sayının toplama işlemi yapılır ardından mod 8 değeri alınır.    
    #İlk kümeden seçilecek x ve y elemanlarının bir listesi ikili_kombinasyonlar oldu.
    fonksiyon = incele(kume1,kume2)
    ikili_kombinasyonlar_ = ikili_kombinasyonlar(copy(kume1))
    #ikili_kombinasyonlar_ = tum_kombinasyonlar(copy(kume1))
    for i in ikili_kombinasyonlar_:
        print(i)
    sayac = 0
    for i in ikili_kombinasyonlar_:
        #Toplamda 6 kombinasyon var. Eğer bu 6 kombinasyonun eşitliği sağlanırsa Ultra Grup Homomorfizması şartlarını sağlayacağından sınıflandırmada sayaç kullanıyorum.
        #Eşitliğin sol tarafının hesaplanması.
        mod = (i[0]+i[1])%8
        #Eşitliğin sağ tarafının hesaplanması.
        mod_ = (fonksiyon[i[0]]+fonksiyon[i[1]])%8
        #Eşitliğin sorgulanması
        try:
            if(fonksiyon[mod]==mod_):
                sonuc = "f([{},{}])=[f({}),f({})] eşitliği sağlandı."
                print(sonuc.format(i[0],i[1],i[0],i[1]))
                sayac = sayac + 1
            else:
                sonuc = "f([{},{}])=[f({}),f({})] eşitliği sağlanmadı!"
                print(sonuc.format(i[0],i[1],i[0],i[1]))
                sayac = 0
        except:
            sonuc = "f([{},{}])=[f({}),f({})] eşitliği sağlanmadı!"
            print(sonuc.format(i[0],i[1],i[0],i[1]))
            sayac = 0
    if(sayac == 6):
        sonuc = str(kume1_)+"---->"+str(kume2)+" M kümeleri arasında Ultra Grup Homomorfizması vardır."
        ugh_saglar.append(sonuc)
        sayac = 0
    else:
        sonuc = str(kume1_)+"---->"+str(kume2)+" M kümeleri arasında Ultra Grup Homomorfizması yoktur."
        ugh_saglamaz.append(sonuc)
        sayac = 0
    print("--------------------------------------------------------------------------------")
    

def ugh_goster():
    print("Ultra Grup Homomorfizması şartını sağlayan küme çiftleri :")
    for saglar in ugh_saglar:
        print(saglar)
    print("--------------------------------------------------------------------------------")
    print("Ultra Grup Homomorfizması şartını sağlamayan küme çiftleri :")
    for saglamaz in ugh_saglamaz:
        print(saglamaz)
    print("--------------------------------------------------------------------------------")
    
#Örnek
#islem([1,2,5,6],[1,2,3,4])