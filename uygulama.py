#Oluşturduğum M kümeleri
from islemler import islem
from normal_alt_ultra import alt_ultra
#Ultra Grup Homomorfizma incelemesi yapmak için kullanılacak metod.
def homomorfizma_incele():
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

#Alt Ultra Grupların normalliğini incelemek için çalıştırılacak olan metod.
def aug_normal_incele(kume):
    #Oluşturulan bu metod parametre olarak küme içerisinde küme alır aksi takdirde hata verebilir.
    #Gönderilecek olan kümeler topluluğu dışarıdan oluşturulup listeye atılıp parametre olarak girilebilir.
    if(len(kume)==0):
        print("Küme içerisinde eleman bulundurmuyor!")
    else:   
        naug_olanlar = list()
        naug_olmayanlar = list()
        for alt_ultra_grup in kume:
            if(alt_ultra(alt_ultra_grup)==1):
                #Normal Alt Ultra Grup olanlar bir listeye eklenecek.
                naug_olanlar.append(alt_ultra_grup)
            else:
                #Normal Alt Ultra Grup olmayanlar bir listeye eklenecek.
                naug_olmayanlar.append(alt_ultra_grup)
        print("Normal Alt Ultra Grup şartlarını sağlayan kümeler:")
        if (len(naug_olanlar)>0):
            for naug in naug_olanlar:
                print(naug)
        else:
            print("- Normal Alt Ultra Grup şartlarını sağlayan herhangi bir küme yok!!")
        print("-----------------------------------------------------")
        print("Normal Alt Ultra Grup şartlarını sağlamayan kümeler:")
        if (len(naug_olmayanlar)>0):    
            for naug_ in naug_olmayanlar:
                print(naug_)
        else:
            print("- Normal Alt Ultra Grup şartlarını sağlamayan herhangi bir küme yok!!")
        print("-----------------------------------------------------")

#aug_normal_incele([[1,2,3,4],[1,2,3,5],[1,6,7,4]])
aug_normal_incele([])