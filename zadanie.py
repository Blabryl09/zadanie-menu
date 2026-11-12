def menu():
    print("1. Pokaż przedmioty")
    print("2. Dodaj przedmioty")
    print("3. Użyj przedmioty")
    print("4. Sprawdz przedmioty")
    print("5. Wyjdz")

def pokaz_ekwipunek(ekwipunek):
    print("Twój Ekwipunek")
    for przedmiot, ilosc in ekwipunek.items():
        print(f"- {przedmiot}: {ilosc}")

def dodaj(ekwipunek):
    dodawanie_itemu = input("Jaki item chcesz dodac? Wpisz: ")
    if dodawanie_itemu in ekwipunek:
        ekwipunek[dodawanie_itemu] += 1
    else:
        ekwipunek[dodawanie_itemu] = 1
    return ekwipunek  
def usun(ekwipunek):
    usun_item = input("Jaki item chcesz usunac? Wpisz: ")
    if usun_item in ekwipunek:
        ekwipunek[usun_item] -= 1
    else:
        print("Nie ma takiego przediotu")
    return ekwipunek
def sprawdz(ekwipunek):
    szukany_item = input("Jaki przedmiot chcesz sprawdzić? Wpisz: ")
    
    if szukany_item in ekwipunek:
        print(f"Masz w ekwipunku: {szukany_item} w ilości {ekwipunek[szukany_item]} szt.")
    else:
        print(f"Nie posiadasz przedmiotu {szukany_item} w ekwipunku.")
    return ekwipunek
def main():
    ekwipunek = {"miecz": 1, "mikstura": 3, "zloto": 50}
    
    while True:
        menu()
        wybor = int(input("Co chcesz robic? Wpisz od (1-5): "))
        if wybor == 5:
            break
        elif wybor == 1:
            pokaz_ekwipunek(ekwipunek)
        elif wybor == 2:
            ekwipunek = dodaj(ekwipunek)  
            print(ekwipunek)
        elif wybor == 3:
            ekwipunek = usun(ekwipunek)
            print(ekwipunek)
        elif wybor == 4:
            ekwipunek = sprawdz(ekwipunek)
            print(ekwipunek)

main()