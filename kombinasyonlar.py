from audioop import reverse
from copy import copy

#Bu fonksiyon kombinasyonların belirli bir kısmını aldı. Normal Alt Ultra Gruplar için tüm kombinasyonlara bakmamız gerekiyor.
#Bu fonksiyon aldığı eleman haricinde ilerisinki elemanlardan seçim yapar.
#Kendisini kendine götüren fonksiyonlar gibi işlemlerde kullanılmaz.
def kombinasyonlar(kume):
    kombinasyonlar = list()
    liste_ = list()
    for i in range(0,len(kume)):
        if(len(kume)>=2):
            z = kume[0]
            kume.remove(kume[0])
            for j in range(0,len(kume)):
                t = kume[j]
                liste_.append(z)
                liste_.append(t)
                kombinasyonlar.append(liste_)
                liste_ = []
    return kombinasyonlar
    


#Bütün kombinasyonları veren fonksiyon
def tum_kombinasyonlar(kume):
    ters_kombinasyonlar = list()
    liste_ = list()
    for i in reversed(range(0,len(kume))):
        for j in reversed(range(0,len(kume))):
            liste_.append(kume[i])
            liste_.append(kume[j])
            ters_kombinasyonlar.append(liste_)
            liste_ = []  
    return ters_kombinasyonlar

#Alt Ultra Grup incelemesinde üç elemanlı kümeleri oluşturmak için.
def uclu_kombinasyon(kume):
    kumeler = list()
    liste_ = list()
    kume_ = copy(kume)
    ilk_eleman = kume[0]
    kume.remove(kume[0])
    ikinci_eleman = kume[0]
    for j in kume:
        liste_.append(ilk_eleman)
        liste_.append(ikinci_eleman)
        liste_.append(j)
        kumeler.append(liste_)
        liste_ = []
    ikinci_eleman = kume[1]
    liste_.append(ilk_eleman)
    liste_.append(ikinci_eleman)
    liste_.append(kume[2])
    kumeler.append(liste_)
    liste_ = []
    for k in kume:
        liste_.append(k)
    kumeler.append(liste_)
    liste_ = []
    kumeler.remove(kumeler[0])
    return kumeler

