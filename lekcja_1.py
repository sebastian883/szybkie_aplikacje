import random
def zgadnij_imie():
    imiona=("Maciek", "Seba", "Kamil")
    imie_do_zgadniecia = random.choice(imiona)

    for próba in range(10):
        zgadnij=input("zgadnij imie: ")
        if zgadnij == imie_do_zgadniecia:
            print("zgadles")
            break
        else:
            print("zle")
            print(f"pozostało prób: {9- próba}")
            próba += 1
        if próba == 10:
            print("sokonczyły ci sie próby")
            break
zgadnij_imie()

