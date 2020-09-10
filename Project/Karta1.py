import Letovi
import datetime
import Logeri

Letovi.dict_Letova()
Lista_karata = []


def Format_Pretraga(x):
    return "{:10}{:10}{:12}{:12}{:13}{:13}{:10}{:15}{:15}{:10}{:10}{:15}{:15}".format(
        x["PASOS"],
        x["BR_LETA"],
        x["POLAZISTE"],
        x["DESTINAIJA"],
        x["VR_POLETANJA"],
        x["VR_SLETANJA"],
        x["SEDISTE"],
        x["DRZAVLJANSTVO"],
        x["DATUM"],
        x["DAN"],
        x["CENA"],
        x["PR_DATUM"],
        x["PRODAVAC"])


def prikaz_k(rLetova, Ime, Prezime, drzavljanstvo, datum_leta, dan, pasos, sediste, pr_datum, uname):
    return '|'.join(
        [Ime, Prezime, drzavljanstvo, rLetova["BR_LETA"], rLetova["POLAZISTE"], rLetova["ODREDISTE"],
         rLetova["VR_POLETANJA"],
         rLetova["VR_SLETANJA"], datum_leta, dan, rLetova["PREVOZNIK"], pasos, sediste,
         rLetova["CENA"], pr_datum, uname])


def upisi_k(karta):
    return '|'.join(
        [karta["IME"], karta["PREZIME"], karta["PASOS"], karta["BR_LETA"], karta["POLAZISTE"], karta["DESTINAIJA"],
         karta["VR_POLETANJA"], karta["VR_SLETANJA"],
         karta["SEDISTE"], karta["DRZAVLJANSTVO"], karta["PREVOZNIK"], karta["DATUM"], karta["DAN"], karta["CENA"],
         karta["PR_DATUM"], karta["PRODAVAC"]])


def provera_datuma(datum_leta, dan):
    DANI = ["pon", "uto", "sre", "cet", "pet", "sub", "ned"]
    pozicija1 = DANI.index(dan)

    date = datetime.datetime.strptime(datum_leta, "%d.%m.%Y")
    if date < datetime.datetime.now():
        print "Datum je u proslosti!"
        Unos_karte("")

    pozicija2 = date.weekday()
    if pozicija1 == pozicija2:
        pass
    else:
        print "Pogresan datum!"
        Unos_karte("")


def Unos_karte(uname):
    unos = raw_input("Unesite Broj Leta :")
    for let in Letovi.l_letovi:
        if let["BR_LETA"] == unos.upper():
            print let["DANI"]
            dan = raw_input("Unesite dan :")
            for dnn in let["DANI"]:
                if dnn == dan:
                    break
            else:
                Unos_karte(uname)
            break

    datum_leta = raw_input("Unesite datum :")
    provera_datuma(datum_leta, dan)

    sediste = raw_input("Unesite sediste : ")
    broj_Sedista(let, sediste)
    sedista = ucitaj_Sedista(unos, datum_leta)

    if sediste in sedista:
        print("Sediste je zauzeto!")
        Unos_karte(uname)

    Ime = raw_input("Unesite Ime :")
    Prezime = raw_input("Unesite Prezime :")
    pasos = raw_input("Unesite broj pasosa :")
    drzavljanstvo = raw_input("Unesite Drzavljansvo :")

    pr_datum = datetime.datetime.now()
    pr_datum = pr_datum.strftime("%d.%m.%Y")

    file = open("karte.txt", "a")
    file.write(prikaz_k(let, Ime, Prezime, pasos, sediste, drzavljanstvo, datum_leta, dan, pr_datum, uname))
    file.write('\n')
    file.close()
    Logeri.p_vrti(uname)




def ucitaj_Sedista(unos, datum_leta):
    sedista = []
    for karta in Lista_karata:
        if karta["BR_LETA"] == unos.upper():
            if karta["DATUM"] == datum_leta:
                sedista.append(karta["SEDISTE"])
    return sedista


def broj_Sedista(let, sediste):
    p_sedista = let["BR_SEDISTA"]
    red, kol = p_sedista.split('/')
    red = int(red)

    kolo = []
    for i in range(int(kol)):
        slovo = (chr(i + 97))
        kolo.append(slovo)
    print kolo

    if int(sediste[:-1]) <= red and sediste[-1] in kolo:
        pass
    else:
        print "Pogresni podaci!"
        Unos_karte("")


def Brisanje_karte():
    global Lista_karata
    Lista_karata = []
    dict_Karata()

    broj_leta = raw_input("Unesi Broj leta:").upper()
    datum_p = raw_input("Datum leta:")
    izbor = raw_input("Pasos ili sediste:")
    parametar = raw_input("Parametar:")

    if izbor == "pasos":
        for karta in Lista_karata:
            if karta["BR_LETA"] == broj_leta and karta["DATUM"] == datum_p and karta["PASOS"] == parametar:
                print "Nadjeno!"
                Lista_karata.remove(karta)
                break
    elif izbor == "sediste":
        for karta in Lista_karata:
            if karta["BR_LETA"] == broj_leta and karta["DATUM"] == datum_p and karta["SEDISTE"] == parametar:
                print "Nadjeno! 2"
                Lista_karata.remove(karta)
                break

    file = open("karte.txt", "w")
    for karta in Lista_karata:
        karta_string = upisi_k(karta)
        file.write(karta_string + "\n")
    file.close()


def izmena_karte(uname):
    global Lista_karata
    Lista_karata = []
    dict_Karata()

    unos = raw_input("Unesite broj leta:").upper()
    datum_p = raw_input("Datum leta:")
    pasos = raw_input("Pasos:")

    for karta in Lista_karata:
        if karta["BR_LETA"] == unos and karta["DATUM"] == datum_p:
            if karta["PASOS"] == pasos:
                break
    else:
        print "Karta nije nadjena."
        izmena_karte(uname)

    broj_let = raw_input("Unesite broj leta:").upper()
    for let in Letovi.l_letovi:
        if let["BR_LETA"] == broj_let:
            print let["DANI"]
            dan = raw_input("Unesite dan :")
            for dnn in let["DANI"]:
                if dnn == dan:
                    break
            else:
                izmena_karte(uname)
            break
    else:
        print("Nepostojeci let!")
        izmena_karte(uname)

    datum_leta = raw_input("Unesite datum :")
    provera_datuma(datum_leta, dan)

    sediste = raw_input("Unesite sediste : ")
    broj_Sedista(let, sediste)
    sedista = ucitaj_Sedista(unos, datum_leta)

    if sediste in sedista:
        print("Sediste je zauzeto!")
        izmena_karte(uname)

    pr_datum = datetime.datetime.now()
    pr_datum = pr_datum.strftime("%d.%m.%Y")

    karta["BR_LETA"] = unos
    karta["POLAZISTE"] = let["POLAZISTE"]
    karta["DESTINACIJA"] = let["ODREDISTE"]
    karta["VR_POLETANJA"] = let["VR_POLETANJA"]
    karta["VR_SLETANJA"] = let["VR_SLETANJA"]
    karta["SEDISTE"] = let["BR_SEDISTA"]
    karta["PREVOZNIK"] = let["PREVOZNIK"]
    karta["DATUM"] = datum_leta
    karta["DAN"] = dan
    karta["CENA"] = let["CENA"]
    karta["PR_DATUM"] = pr_datum

    file = open("karte.txt", "w")
    for karta in Lista_karata:
        karta_string = upisi_k(karta)
        file.write(karta_string + "\n")
    file.close()
    Logeri.p_vrti(uname)


def r_karata(line):
    if line[-1] == "\n":
        line = line[:-1]
    ime, prezime, pasos, br_leta, polaziste, destinacija, vr_poletanja, vr_sletanja, sediste, drzavljanstvo, prevoznik, datum, dan, cena, pr_datum, uname = line.split(
        "|")
    r_karata = {

        "IME": ime,
        "PREZIME": prezime,
        "PASOS": pasos,
        "BR_LETA": br_leta,
        "POLAZISTE": polaziste,
        "DESTINAIJA": destinacija,
        "VR_POLETANJA": vr_poletanja,
        "VR_SLETANJA": vr_sletanja,
        "SEDISTE": sediste,
        "DRZAVLJANSTVO": drzavljanstvo,
        "PREVOZNIK": prevoznik,
        "DATUM": datum,
        "DAN": dan,
        "CENA": cena,
        "PR_DATUM": pr_datum,
        "PRODAVAC": uname
    }

    return r_karata


def dict_Karata():
    for line in open("karte.txt", "r").readlines():
        recnik_karata = r_karata(line)
        Lista_karata.append(recnik_karata)


def pretraga_menadzer_1(parametar):
    global Lista_karata
    Lista_karata = []
    dict_Karata()

    datum = raw_input("Datum:")

    print "{:10}{:10}{:12}{:12}{:13}{:13}{:10}{:15}{:15}{:10}{:10}{:15}{:15}".format("PASOS", "BR_LETA", "POLAZISTE",
                                                                                     "DESTIACIJA", "VR_POLETANJA",
                                                                                     "VR_SLETANJA", "SEDISTE",
                                                                                     "DRZAVLJANSTVO", "DATUM", "DAN",
                                                                                     "CENA", "PR_DATUM", "PRODAVAC")
    print "-" * 190

    for karta in Lista_karata:
        if karta[parametar] == datum:
            str_karta = Format_Pretraga(karta)
            print str_karta


def pretraga_menadzer_2():
    global Lista_karata
    Lista_karata = []
    dict_Karata()
    datum = raw_input("Unesite datum :")
    prodavac = raw_input("Unesite Prodavca :")
    print "{:10}{:10}{:12}{:12}{:13}{:13}{:10}{:15}{:15}{:10}{:10}{:15}{:15}".format("PASOS", "BR_LETA", "POLAZISTE",
                                                                                     "DESTIACIJA", "VR_POLETANJA",
                                                                                     "VR_SLETANJA", "SEDISTE",
                                                                                     "DRZAVLJANSTVO", "DATUM", "DAN",
                                                                                     "CENA", "PR_DATUM", "PRODAVAC")
    print "-" * 190
    for karta in Lista_karata:
        if datum == karta["PR_DATUM"] and prodavac == karta["PRODAVAC"]:
            str_karta = Format_Pretraga(karta)
            print str_karta


def pretraga_menadzer_3(parametar):
    global Lista_karata
    Lista_karata = []
    dict_Karata()
    cena = 0

    datum = raw_input("Unesite datum : ")
    for karta in Lista_karata:
        if karta[parametar] == datum:
            cena = cena + int(karta["CENA"])

    print "Ukupna cena je ", cena


def pretraga_menadzer_2():
    global Lista_karata
    Lista_karata = []
    dict_Karata()
    cena = 0

    datum = raw_input("Unesite datum :")
    prodavac = raw_input("Unesite Prodavca :")

    for karta in Lista_karata:
        if karta["PR_DATUM"] == datum and karta["PRODAVAC"] == prodavac:
            cena = cena + int(karta["CENA"])

    print "Ukupna cena je", cena


def pretraga_menadzer_4():
    global Lista_karata
    Lista_karata = []
    dict_Karata()
    cena = 0
    trenutno = datetime.datetime.now()
    dana_30 = datetime.timedelta(days=30)
    ogranici = trenutno - dana_30
    prodavac = raw_input("unesi ime prodavca")
    for karta in Lista_karata:
        if prodavac == karta["PRODAVAC"]:
            for karta in Lista_karata:
                date = datetime.datetime.strptime(karta["DATUM"], "%d.%m.%Y")
                if date > ogranici:
                    cena = cena+int(karta["CENA"])
        break

    print cena






dict_Karata()
