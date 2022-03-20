def alpha(kume,H):
    #Sonuçları döndüren boş liste.
    liste = list()
    #Sonuçların içine atılacak satırların listesi.
    ilk_liste = list()
    #Önce H ile işleme tabi tutmadan hesaplama yapıyoruz.
    for i in kume:
        for j in kume:
            sonuc = (i + j)%8
            ilk_liste.append(sonuc)
        liste.append(ilk_liste)
        ilk_liste=[]
    #H ile işleme tabi tutup listedeki sonuç değerlerini güncelliyoruz.
    for satir in range(0,len(liste)):
        for eleman in range(0,len(liste[satir])):
            for i in H:
                mod = (liste[satir][eleman] + i)%8
                if(mod in kume):
                    liste[satir][eleman]=mod
    return liste


