from copy import copy
from kombinasyonlar import tum_kombinasyonlar
#Bu modül alt ultra gruplarının Normallik şartlarını karşılayıp karşılamadıklarını denetler.
#Formül
#Ele alınan alt ultra grubunun ikili kombinasyonları olacak şekilde x ve y olarak elemanları alınır.
#[x,[x,y]] = [{x,y},[x,y]]

#İlk işlem alınacak olan ultra grubun elemanlarının kombinasyonlarının alınması.
kombinasyonlar_ = list()
#Seçilen ikililerin geçici olarak alınacağı liste liste_ olacak.
def alt_ultra(kume):
    #Bellek adresinden verileri ayırmak için kopyaladık.
    kume_ = copy(kume)
    #Eşitliği sağlamayan bir eleman olduğu zaman bu sayaç artacak ve Normal Alt Ultra Grup olmadığını belirtecek.
    esitlik_sayac = 0
    esitlik_saglamayanlar = list()
    kombinasyonlar_ = tum_kombinasyonlar(kume)
    #Böylece alt ultra gruplardan alacağımız x ve y eleman çiflerine ulaşacağız.
    #Bu fonksiyon aynı zamanda ters yönde de çalıştırılmalı bütün x ve y çiftlerine bakmalıyız.!
    for ikililer in kombinasyonlar_:
        print("x = "+str(ikililer[0])+" , "+"y = "+str(ikililer[1])+" ikilisi için işlem sonuçları:")
        #Formüldeki eşitliğin sol tarafının hesaplanması.
        mod = (ikililer[0]+((ikililer[0]+ikililer[1])%8))%8
        mod_ =(((ikililer[0]+((ikililer[0]+ikililer[1])%8))%8)+((ikililer[1]+((ikililer[0]+ikililer[1])%8))%8))%8
        if(mod == mod_):
            sonuc = "[{},[{},{}]] = [{{{},{}}},[{},{}]] eşitliği sağlandı.\n"
        else:
            sonuc = "[{},[{},{}]] = [{{{},{}}},[{},{}]] eşitliği sağlanmadı!\n"
            esitlik_sayac = 1
        #Sol ve sağdaki işlemlerin sonuç olarak ne verdiğini görmek için.
        sonuc1 = "[{},[{},{}]] = "+str(mod)
        sonuc2 = "[{{{},{}}},[{},{}]] = "+str(mod_)
        print(sonuc1.format(ikililer[0],ikililer[0],ikililer[1]))
        print(sonuc2.format(ikililer[0],ikililer[1],ikililer[0],ikililer[1]))
        print(sonuc.format(ikililer[0],ikililer[0],ikililer[1],ikililer[0],ikililer[1],ikililer[0],ikililer[1]))
    #Bu fonksiyon diğer modüllerde kullanılacağı için eğer gönderilen kume parametresi Normal Alt Ultra Grup belirtiyorsa 1, özellikleri sağlamıyor ise 0 değerini gönderiyoruz.
    if(esitlik_saglamayanlar == 0):
        print(str(kume_)+" bir Normal Alt Ultra Gruptur.\n")
        return 1
    else:
        print(str(kume_)+" bir Normal Alt Ultra Grup değildir!\n----------------------------")
        return 0

    
