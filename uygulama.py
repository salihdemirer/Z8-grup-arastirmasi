#Oluşturduğum M kümeleri
from islemler import islem

M = [[0,1,2,3],[0,1,2,7],[0,1,6,3],[0,1,6,7],[0,5,2,3],[0,5,2,7],[0,5,6,3],[0,5,6,7]]
# M kümeleri arasında karşılaştırma yapmak için kombinasyonlara ihtiyacım var.
kombinasyonlar = list()
liste_ = list()
for i in range(0,len(M)):
    if(len(M)>=2):
        z = M[0]
        M.remove(M[0])
        for j in range(0,len(M)):
            t = M[j]
            liste_.append(z)
            liste_.append(t)
            kombinasyonlar.append(liste_)
            liste_ = []
for i in kombinasyonlar:
    print(i)
for i in kombinasyonlar:
    #print(str(i[0])+"--->"+str(i[1]))
    islem(i[0],i[1])
    #kontrol_islem(i[1],i[0])
#M8 yani son grupları atladı işleme almadı bu ikililer arasında değişmeli çalışmam gerek yani kombinasyonları düzenle.
