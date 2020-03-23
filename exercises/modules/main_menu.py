import modules.main_body as main
import inspect

#Nakladka Menu do funkcji
#def mainmenu
licznikmenu=0
while licznikmenu < 1:
    print("Witaj w Multitool Python Program by iSA - wersja beta \n Wybierz program, który cię interesuje:")
    menu={}
    for idx, i in enumerate(dir(main)):
        menu[idx] = i
        print(idx, i)
    numer_funkcji = input("Podaj numer funkcji z powyzszej listy: ")
    try:
        id_funkcji = int(numer_funkcji)
    except:
        print("Niepoprawny numer funkcji")

    if  id_funkcji in menu.keys():
        nazwa_funkcji=menu[id_funkcji]
        print(f"Wybrales funkcje: "+nazwa_funkcji)
        funkcja = getattr(main, nazwa_funkcji)
        parametr = inspect.getfullargspec(funkcja).args
        print(parametr)
        #funkcja()
        licznikmenu += 1
    else:
        print("Nie wybrales zadnego programu")

    # if numer_funkcji in menu.idx:
    #
    # for idx, i in enumerate(menu):
    #     print(idx, i)
    #
    #     if