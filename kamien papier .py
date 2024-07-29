import random
def gra_kamien_papier_nozyce():
 ruchy = ("kamien", "papier", "nozyce") #github
 for próba in range(15):
        pozostałe_próby = 15- próba
        print(f" pozostalo prób: {pozostałe_próby}")
        ruch_gracza=input(" wybierz ruch (kamien, papier, nozyce): ")
        ruch_komputera =random.choice(ruchy)
        print(f"ruch komputera to: {ruch_komputera}")
        if ruch_gracza == ruch_komputera:
            print("remis")
        elif (ruch_komputera == "kamien" and ruch_gracza == "nozyce") or  (ruch_komputera == "papier" and ruch_gracza == "kamien") or (ruch_komputera == "nozyce" and ruch_gracza == "papier"):
             print("przegrales")
        else:
            print("wygrałes")

gra_kamien_papier_nozyce()




