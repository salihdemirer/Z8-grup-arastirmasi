from audioop import reverse

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
kombinasyon = tum_kombinasyonlar([1,2,3,4])
print("Programın deneyeceği kombinasyonlar:")
for i in kombinasyon:
    print(i)
print("Programın deneyeceği kombinasyon sayısı:")
print(len(kombinasyon))