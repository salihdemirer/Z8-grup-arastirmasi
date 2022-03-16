#G=(Z8,+) (işlem + mod 8)
#ID = {0}
from matplotlib.pyplot import table
import pandas
from IPython.display import display, HTML
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

