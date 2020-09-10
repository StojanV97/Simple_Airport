import Logeri


def prikaz(rLetova):
    return '|'.join([rLetova["BR_LETA"],rLetova["POLAZISTE"],rLetova["ODREDISTE"],rLetova["VR_POLETANJA"],
                    rLetova["VR_SLETANJA"],rLetova["PREVOZNIK"],rLetova["BR_SEDISTA"],rLetova["CENA"]])





def Pretraga_let(s):
    b = raw_input("Unesite : ").upper()
    print "{:12}{:12}{:12}{:18}{:18}{:30}{:30}{:10}".format("Broj leta","Polaziste","Odlaziste","Vreme poletanja","Vreme sletanja","Dani","Prevoznik","Sedista")
    print "=" * 150
    for let in l_letovi:
        if b == let[s]:
            #print prikaz(let)
            print Format_Pretraga(let)
            #Lista_karata.append(let)
    #Stampanje_karte()
  #  print Lista_karata



def P_Letova():
    print " 1 ----> Mesto polaska"
    print " 2 ----> Odrediste"
    print " 3 ----> Dani"
    print " 4 ----> Vreme poletanja"
    print " 5 ----> Vreme sletanja"
    print " 6 ----> Prevoznik"
    print " 7 ----> Odjava"

    a = raw_input("Unesite : ")
    s = ""
    if a == "1":
        s = "POLAZISTE"
    elif a == "2":
            s = "ODREDISTE"
    elif a == "3":
        b = raw_input("Unesi : ")
        for let in l_letovi:
            if let["DANI"]:
                for svoow in let["DANI"]:
                    if svoow == b:
                        print Format_Pretraga(let)
    elif a == "4":
        s = "VR_POLETANJA"
    elif a == "5":
        s = "VR_SLETANJA"
    elif a == "6":
        s = "PREVOZNIK"
    elif a == "7":
        return False
    if s != "":
        Pretraga_let(s)


def letovi(line):
    if line[-1] == '\n':
        line = line[:-1]
    br_leta, polaziste, odrediste, vr_poletnja, vr_sletanja, prevoznik, dani, br_sedista, cena = line.split("|")
    dani = dani.split(',')
    rLetova = {
        "BR_LETA": br_leta,
        "POLAZISTE": polaziste,
        "ODREDISTE": odrediste,
        "VR_POLETANJA": vr_poletnja,
        "VR_SLETANJA": vr_sletanja,
        "PREVOZNIK": prevoznik,
        "DANI": dani,
        "BR_SEDISTA": br_sedista,
        "CENA": cena
    }

    return rLetova


def dict_Letova():
    for line in open("Letovi.txt", "r").readlines():
        recnik_letova = letovi(line)
        l_letovi.append(recnik_letova)


l_letovi = []


def Format_Pretraga(rLetova):
    dani = ','.join(rLetova["DANI"])
    return "{:12}{:12}{:12}{:18}{:18}{:30}{:30}{:10}".format(rLetova["BR_LETA"],
                                                       rLetova["POLAZISTE"],
                                                       rLetova["ODREDISTE"],
                                                       rLetova["VR_POLETANJA"],
                                                       rLetova["VR_SLETANJA"],
                                                       dani,
                                                       rLetova["PREVOZNIK"],
                                                       rLetova["BR_SEDISTA"],
                                                       )
