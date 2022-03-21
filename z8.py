#G=(Z8,+) (işlem + mod 8)
#ID = {0}
from copy import copy
import re
from prettytable import PrettyTable as pt
from kombinasyonlar import kombinasyonlar, uclu_kombinasyon, tum_kombinasyonlar
from normal_alt_ultra import alt_ultra
from alpha import alpha
z8 = (0,1,2,3,4,5,6,7)
# liste_ = list()
# satirlar = list()
ug_olanlar = list()
ug_olmayanlar = list()
aug_olanlar = list()
aug_olmayanlar = list()
#İlk satırı yazdıralım
def grup_yazdir():
    print("Z8 = {0,1,2,3,4,5,6,7}")
    print("Birim eleman = {0} ")
    print("Tablo:")
    satirlar = list()
    liste_ = list()
    for eleman in z8:
        for j in range(0,len(z8)):
            sonuc =(eleman+z8[j])%8
            liste_.append(sonuc)
        satirlar.append(liste_)
        liste_ = []
    tb = pt()
    tb.field_names = z8
    satirlar.remove(satirlar[0])
    for i in satirlar:
        tb.add_row(i)
    print(tb)
    print("------------------------------------------------------")


M = [[0,1,2,3],[0,1,2,7],[0,1,6,3],[0,1,6,7],[0,5,2,3],[0,5,2,7],[0,5,6,3],[0,5,6,7]]
K = [[0,1,2,3],[0,1,2,7],[0,1,6,3],[0,1,6,7],[0,5,2,3],[0,5,2,7],[0,5,6,3],[0,5,6,7]]
H = [0,4]
#Ultra Grup incelemesi

def tablo_olustur(kume,H,sonuc_listesi,ilk_eleman):
    tb = pt()
    ilk_satir = list()
    satirlar_ = list()
    if(ilk_eleman == "alfa"):
        ilk_satir.append(ilk_eleman)
        for i in kume:
            ilk_satir.append(str(i))
    if(ilk_eleman == "beta"):
        ilk_satir.append(ilk_eleman)
        for i in H:
            ilk_satir.append(str(i))
        #İlk satır tamamlandı
    tb.field_names = ilk_satir
    for j in range(0,len(kume)):
        satirlar = list()
        satirlar.append(str(kume[j]))
        # for k in range(0,len(sonuc_listesi)):
        for l in range(0,len(sonuc_listesi[j])):
            satirlar.append(str(sonuc_listesi[j][l]))
        satirlar_.append(satirlar)
    satirlar = []
    for eleman in satirlar_:
        tb.add_row(eleman)
    print(tb)


def eleman_kontrol(m_kume,satirlar):
    #Sonuç kısmında oluşturulan kümelerin elemanlarının M kümesinde olup olmadığının kontrolünü yapan metod.
    for satir in satirlar:
        for eleman in satir:
            if(eleman not in m_kume):
                return 0
    return 1

#Alfa işlemlerinin incelenmesi
def alpha_islemi(kume):
    #Kodlar yazılırken ele alınan kümeler dışında değerler verildiğinde hata döndürüyor.
    print("Alfa işlemi:")
    sonuc_listesi = alpha(kume,H)
    tablo_olustur(kume,"",sonuc_listesi,"alfa")
    kontrol = eleman_kontrol(kume,sonuc_listesi)
    return kontrol
    
def beta_islemi(kume):
    print("Beta işlemi:")
    sonuc_listesi = list()
    satir = list()
    for eleman in kume:
        for eleman1 in H:
            mod = (eleman + eleman1)%8
            mod_ = (eleman1+mod)%8
            if(mod_ in kume):
                if(len(satir)<2):
                    satir.append(mod_)
                else:
                    sonuc_listesi.append(satir)
                    satir = []
                    satir.append(mod_)
    sonuc_listesi.append(satir)
    satir = []
    tablo_olustur(kume,H,sonuc_listesi,"beta")
    kontrol = eleman_kontrol(kume,sonuc_listesi)
    return kontrol

def ultra_grup_kontrol(kume):
    # alpha_islemi(kume)
    # beta_islemi(kume)
    print("----------------------------------------------------------\n")
    print(str(kume)+" için Ultra Grup sorgu işlem sonuçları:\n")
    kontrol1 = alpha_islemi(kume)
    kontrol2 = beta_islemi(kume)
    if(kontrol1 == 1 and kontrol2 == 1):
        print(str(kume)+" bir Ultra Gruptur.")
        ug_olanlar.append(kume)
    else:
        print(str(kume)+" bir Ultra Grup değildir!")
        ug_olmayanlar.append(kume)
    print("----------------------------------------------------------\n")

def alt_ultra_grup(kume):
    kume__ = copy(kume)
    kume_ = copy(kume)
    bas = kombinasyonlar(kume)#Burada iki elemanlı küme kombinasyonları
    kuyruk = uclu_kombinasyon(kume_)#Burada üç elemanlı küme kombinasyonları
    bas.extend(kuyruk)
    #İkili ve üçlü kombinasyon kümelerini baş ve kuyruk olarak adlandırıp hesaplayıp tek kümede birleştirdik.
    for eleman in bas:
        kontrol1 = alpha_islemi(eleman)
        kontrol2 = beta_islemi(eleman)
        if(kontrol1 == 1 and kontrol2 == 1):
            print(str(eleman)+" bir alt ultra gruptur.")
            aug_olanlar.append(eleman)
        else:
            print(str(eleman)+" bir alt ultra grup değildir.")
            aug_olmayanlar.append(eleman)
    print("--------------------------------------------")
    print(str(kume__)+" için Alt Ultra Gruplar:\n")
    for i in range(0,len(aug_olanlar)):
        print(str(i+1)+"-"+str(aug_olanlar[i]))
    print("--------------------------------------------")
    print(str(kume__)+" için Alt Ultra Grup olmayanlar:\n")
    for i in range(0,len(aug_olmayanlar)):
        print(str(i+1)+"-"+str(aug_olmayanlar[i]))
    print("--------------------------------------------")

def normal_alt_ultra_grup():
    for eleman in aug_olanlar:
        print(str(eleman)+" kümesi için inceleme:\n")
        sonuc = alt_ultra(eleman)
        if(sonuc == 1):
            print(str(eleman)+" bir Normal Alt Ultra Gruptur.")
        else:
            print(str(eleman)+" bir Normal Alt Ultra Grup değildir.")
        print("------------------------------------------------------")
def ultra_grup_homomorfizma(M):
    #Formül
    #f([x,y])=[f(x),f(y)]
    kombinasyonlar_ = list()
    kombinasyonlar__ = tum_kombinasyonlar(M)
    #Tüm kombinasyonlar tersten oluşmuştu, tekrar tersine çevirdik.
    kombinasyonlar_ = list(reversed(kombinasyonlar__))
    fonksiyonlar = list()
    for ikili in kombinasyonlar_:
        fonksiyon = dict()
        for i in range (0,len(ikili[0])):
            fonksiyon[ikili[0][i]]=ikili[1][i]
        #f([x,y]) sol işlemi
        #Seçilecek x ve y elemanları için kombinasyonlar oluşturduk.
        komb = list(reversed(tum_kombinasyonlar(ikili[0])))
        for eleman in komb:
            mod = (eleman[0] + eleman[1])%8
            for i in H:
                mod_ = (i + mod)%8
                if(mod_ in ikili[0]):
                    mod__ = mod
            try:
                sol_taraf = fonksiyon[mod__]
                #Sağ taraf işlemleri
                eleman1 = fonksiyon[eleman[0]]
                eleman2 = fonksiyon[eleman[1]]
                imod = (eleman1 + eleman2)%8
                for j in H:
                    imod_ = (j + imod)%8
                    if(imod_ in ikili[1]):
                        sag_taraf = imod_
                print("------------------------------------------------")
                sonuc = "f([{},{}])=[f({}),f({})]"
                sonuc_ = "{} = {}"
                print(sonuc.format(eleman[0],eleman[1],eleman[0],eleman[1]))
                print(sonuc_.format(sol_taraf,sag_taraf))
                if (sol_taraf == sag_taraf):
                    print(str(ikili[0])+" --->"+str(ikili[1])+" fonksiyonunda "+ str(eleman) +" için Ultra Grup Homomorfizması vardır.")
                else:
                    print(str(ikili[0])+" --->"+str(ikili[1])+" fonksiyonunda "+ str(eleman) +" için Ultra Grup Homomorfizması yoktur.")
                print("------------------------------------------------")
            except:

                print(str(ikili[0])+" --->"+str(ikili[1])+" fonksiyonunda "+ str(eleman) +" için Ultra Grup Homomorfizması yoktur.")

def sonuc_yazdir():
    k = copy(M)           
    for i in k:
        ultra_grup_kontrol(i)
    print("Ultra Grup şartlarını sağlayanlar:")
    if(len(ug_olanlar)>0):
        for i in ug_olanlar:
            print(" -"+str(i))
    else:
        print(" -Ultra Grup şartlarını sağlayan eleman yok!")
    print("Ultra Grup şartlarını sağlamayanlar:")
    if(len(ug_olmayanlar)>0):
        for i in ug_olmayanlar:
            print(" -"+str(i))
    else:
        print(" -Ultra Grup şartlarını sağlamayan eleman yok!")
    print("-------------------------------------------------------\n")
    for j in M:
        alt_ultra_grup(j)
    normal_alt_ultra_grup()
    ultra_grup_homomorfizma(K)

#ultra_grup_homomorfizma(M)
#alt_ultra_grup([0,1,2,3])
#normal_alt_ultra_grup()
#grup_yazdir()
#alt_ultra_grup([0,1,6,3])
#alpha_islemi([0,1])
#(alpha_islemi([0,1,2,3]))
#beta_islemi([0,1,2,3])
#ultra_grup_kontrol([0,1,2,3])
sonuc_yazdir()
# for i in M:
#     ultra_grup_kontrol(i)
# print(M)
# print(K)
# ultra_grup_homomorfizma(K)
