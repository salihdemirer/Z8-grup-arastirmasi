#G=(Z8,+) (işlem + mod 8)
#ID = {0}
from copy import copy
import re
from traceback import print_tb
import pandas
from prettytable import PrettyTable as pt
from kombinasyonlar import kombinasyonlar, uclu_kombinasyon

z8 = (0,1,2,3,4,5,6,7)
liste_ = list()
satirlar = list()
#İlk satırı yazdıralım
for eleman in z8:
    for j in range(0,8):
        sonuc =(eleman+z8[j])%8
        liste_.append(sonuc)
    satirlar.append(liste_)
    liste_ = []
#Tabloyu yazdırmak için
tablo = pandas.DataFrame(satirlar)
print(tablo)

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
    sonuc_listesi = list()
    satir = list()
    for eleman1 in kume:
        for eleman2 in kume:
            mod = (eleman1+eleman2)%8
            for eleman3 in H:
                sonuc = (eleman3+mod)%8
                if sonuc in kume:
                    if(len(satir)<len(kume)):
                        satir.append(sonuc)
                    else:
                        sonuc_listesi.append(satir)
                        satir = []
                        satir.append(sonuc)
                    #Burası eleman olan sayıyı eklemeli.eleman olmayan sayıyı bildirmeli!
    sonuc_listesi.append(satir)
    satir = []
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
    kume_ = copy(kume)
    bas = kombinasyonlar(kume)#Burada iki elemanlı küme kombinasyonları
    kuyruk = uclu_kombinasyon(kume_)#Burada üç elemanlı küme kombinasyonları
    bas.extend(kuyruk)
    print(bas)
    #İkili ve üçlü kombinasyon kümelerini baş ve kuyruk olarak adlandırıp hesaplayıp tek kümede birleştirdik.
    for eleman in bas:
        kontrol1 = alpha_islemi(eleman)
        kontrol2 = beta_islemi(eleman)
        if(kontrol1 == 1 and kontrol2 == 1):
            print(str(eleman)+" bir alt ultra gruptur.")
        else:
            print(str(eleman)+" bir alt ultra grup değildir.")


#alt_ultra_grup([0,1,6,7])
alpha_islemi([0,1])
#(alpha_islemi([0,1,2,3]))
#beta_islemi([0,1,2,3])
#ultra_grup_kontrol([0,1,2,3])
