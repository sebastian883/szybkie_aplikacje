import random
def kamien_papier_nozyce():
    ruchy = ("kamien", "papier", "nozyce")
    for próba in range(20):
        wybor_komputera = random.choice(ruchy)
        wybor_gracza=input("wybierz ruch: kamien, papier, nozyce: ")
        if wybor_gracza == wybor_komputera:
            print(f"remis! wybor komputera to rowniez {wybor_komputera}")
            print(f"pozostalo prob {19 - próba}")
        elif (wybor_gracza == "kamien" and wybor_komputera == "nozyce") or\
             (wybor_gracza == "nozyce" and wybor_komputera == "papier") or\
             (wybor_gracza == "papier" and wybor_komputera == "kamien"):
             print(f"wygrales! wybor komputera to {wybor_komputera}")
             break
        elif wybor_gracza not in ruchy:
            print("nie ma takiego wyboru")
            print(f"pozostalo prob {19 - próba}")
        else:
            print(f"przegrales! wybor komputera to {wybor_komputera}")
            print(f"pozostalo prob {19 - próba}")
kamien_papier_nozyce()





