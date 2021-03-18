import random

def start_game():

    lines = open('slova.txt').read().splitlines()

    slovo = random.choice(lines)

    slovo_list = list(slovo)
    slovo_list_cover = []

    for i in range(0, len(slovo)):
        slovo_list_cover.append("*")

    #iba vypisanie na začiatku
    pocet_n = int(input("Zadajte počet pokusov ktoré chcete mať: "))

    y = ""
    i = 0
    #začína kontrolavt
    pokusy  = pocet_n
    while i+1 <= pocet_n:

        print("Slovo: ", end="")
        print("".join(slovo_list_cover))
        print("Neobsahuje: "+y)
        print("Ostáva vám ešte " + str(pokusy) + " pokusy")

        x = input("Vyber ďalšie písmeno: ")
        counter = 0
        for j in range(0, len(slovo)):
            if x == slovo_list[j]:
                slovo_list_cover[j] = x
                counter += 1

            elif counter == 0 and j == len(slovo) - 1:
                y = y + x + " , "
                i += 1
                pokusy = pocet_n - i
                break

        if "*" not in slovo_list_cover:
            print("!!!Vyhrali ste!!!")
            print("Ukryté slovo: "+ slovo)
            break

        print("__________")
        print("__________")
        print("__________")
        print("__________")

    if "*" in slovo_list_cover:
        print("Prehrali ste!!!")
        print("Ukryté slovo bolo: "+ slovo)

start_game()
input()













