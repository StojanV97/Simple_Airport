import Logeri
import Letovi



def main():
    Letovi.dict_Letova()
    print "Ulogujte se:"
    zanimanje, uname = Logeri.loger()
    while zanimanje == 0:
        zanimanje, uname = Logeri.loger()
    if zanimanje == "m":
        Logeri.m_vrti()
    elif zanimanje == "p":
        Logeri.p_vrti(uname)

if __name__ == "__main__":
    main()