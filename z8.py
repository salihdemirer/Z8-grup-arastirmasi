#G=(Z8,+) (işlem + mod 8)
#ID = {0}
from copy import copy
import re
from prettytable import PrettyTable as pt
from kombinasyonlar import kombinasyonlar, uclu_kombinasyon
from alpha import alpha

z8 = (0,1,2,3,4,5,6,7)
# liste_ = list()
# satirlar = list()
aug_olanlar = list()
aug_olmayanlar = list()
#İlk satırı yazdıralım
def grup_yazdir():
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


M = [[0,1,2,3],[0,1,2,7],[0,1,6,3],[0,1,6,7],[0,5,2,3],[0,5,2,7],[0,5,6,3],[0,5,6,7]]
H = [0,4]
#Ultra Grup incelemesi

def tablo_olustur(kume,H,sonuc_listesi,ilk_eleman):
    tb = pt()
    ilk_satir = list()
    satirlar_ = list()
    if(ilk_eleman == "α"):
        ilk_satir.append(ilk_eleman)
        for i in kume:
            ilk_satir.append(str(i))
    if(ilk_eleman == "β"):
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
    tablo_olustur(kume,"",sonuc_listesi,"α")
    kontrol = eleman_kontrol(kume,sonuc_listesi)
    return kontrol
    #Burada görüntüleme işlemini daha kolay yapabilir miyim?
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
    tablo_olustur(kume,H,sonuc_listesi,"β")
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
    else:
        print(str(kume)+" bir Ultra Grup değildir!")
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



grup_yazdir()
#alt_ultra_grup([0,1,6,3])
#alpha_islemi([0,1])
#(alpha_islemi([0,1,2,3]))
#beta_islemi([0,1,2,3])
#ultra_grup_kontrol([0,1,2,3])
