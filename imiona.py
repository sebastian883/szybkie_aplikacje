import random
def zgadnij_imie():
    imiona=("Maciek", "Seba", "Kamil")
    imie_do_zgadniecia = random.choice(imiona)

    for próba in range(10):
        pozostale_próby = 10- próba
        print(f" pozostalo prób: {pozostale_próby}")
        zgadnij=input("zgadnij imie: ")
        if zgadnij == imie_do_zgadniecia:
            print("zgadles")
            break
        else:
            print("zle")
        if próba == 10:
            print("sokonczyły ci sie próby")
            break
zgadnij_imie()
