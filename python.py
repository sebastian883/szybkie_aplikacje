import random
def zgadnij_imie():
    imiona = ("sebastian", "mateusz", "kamil")
    imie_do_zgadnięcia=random.choice(imiona)
    for próba in range (10):
        zgadnij=input("zgadnij imie: sebastian, mateusz lub kamil ")
        if zgadnij == imie_do_zgadnięcia:
            print("brawo! zgadłes")
            break
        elif zgadnij not in imiona:
            print(f"nie ma takiego wyboru! pozostało prób: {9 - próba} ")
        else:
            print(f"nie zgadłes! pozostało prób: {9 - próba}")
zgadnij_imie()


