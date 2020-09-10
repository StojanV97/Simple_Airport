import Letovi
import projekat
import Karta1


def loger():
    uname = raw_input("unesite korisnicko ime : ")
    pname = raw_input("unesi lozinku : ")
    file = open("Menadzer.txt","r")
    for line in file:
        f = line.split("!")
        if uname == f[0] and f[1].strip() == pname:
            file.close()
            return 'm', uname
    else:
        file = open("prodavaci.txt","r")
        for line in file:
            f = line.split("!")
            if uname == f[0] and f[1].strip() == pname:
                file.close()
                return 'p', uname
        else:
            print "Neuspesno, pokusajte ponovo."
            return 0, 0


def m_vrti():
    print " 1 ----> Pretraga"
    print " 2 ----> Istorija"
    print " 3 ----> Odjava"
    print " 4 ----> Izadji"

    p = raw_input("Izaberite opciju:")
    if p == "1":
        Letovi.P_Letova()
    elif p == "2":
        istorija()
    elif p == "3":
        projekat.main()
    elif p == "4":
        exit()
    m_vrti()

def istorija():
    print "1 ----> Po datumu prodaje"
    print "2 ----> Po datumu polaska"
    print "3 ----> Po datumu prodaje i prodavcu"
    print "4 ----> Ukupna cena za dan prodaje"
    print "5 ----> Ukupna cena za dan polaska"
    print "6 ----> Ukupna cena za dan prodaje i prodavca"
    print "7 ----> Ukupna cena za poslednjih 30 dana"
    print "8 ----> Nazad"
    p = raw_input("Izaberite opciju:")

    if p == "1":   
        parametar = "PR_DATUM"
        Karta1.pretraga_menadzer_1(parametar)
    elif p == "2":
        parametar = "DATUM"
        Karta1.pretraga_menadzer_1(parametar)
    elif p == "3":
        Karta1.pretraga_menadzer_2()
    elif p == "4":
        parametar = "PR_DATUM" 
        Karta1.pretraga_menadzer_3(parametar)
    elif p == "5":
        parametar = "DATUM"
        Karta1.pretraga_menadzer_3(parametar)
    elif p == "6":
        Karta1.pretraga_menadzer_2()
    elif p == "7":
        Karta1.pretraga_menadzer_4()
    elif p == "8":
        m_vrti()
    istorija() 



def p_vrti(uname):
    print " 1 ----> Pretraga"
    print " 2 ----> Unos karte"
    print " 3 ----> Izmena karte"
    print " 4 ----> Brisanje karte"
    print " 5 ----> Odjava"
    print " 6 ----> Izadji"

    p = raw_input("Izaberi opciju:")
    if p == "1":
        Letovi.P_Letova()
    elif p == "2":
        Karta1.Unos_karte(uname)
    elif p == "3":
        Karta1.izmena_karte(uname)
    elif p == "4":
        Karta1.Brisanje_karte()
    elif p == "5":
        projekat.main()
    elif p == "6":
        exit()
    p_vrti(uname)

