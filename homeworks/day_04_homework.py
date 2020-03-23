# Od dziś też będę zwaracał uwagę na to czy nie tylko kod działa ale:
# a) czy składanie jest ładna i zgodna ze standardami
# b) czy kod jest zabezpieczony przed wprowadzaniem niepoprawnych danych
#    (np jeśli prosimy o liczbę a dostaniemy znaki poprośmy użytkownika o podanie danej jeszcze raz)
# c) czy metody są udokumentowane a co ciekawsze fragmentu kodu opatrzone komentarzem.
# d) parametryzacja, im większy wpływ na program i jakieś parametry tym fajniej :)
# e) wydzielanie uniwersalnych fragmentów kodów do osobnych funckji
#

# Zadania:
# 1) Prośba o przepisanie dotychczasowych proagramów z wykorzystaniem definiowania własnych funkcji i wytycznych powyżej
#day_02_homework_new.py
# 2) Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
#    Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
#    Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
#    A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn :)
lista2 = [x for x in input("Podaj listę wartości, oddzielonymi spacją: ").split()]

for idx,i in enumerate(lista2):
    len_i=len(i)
    len_list = len(lista2)
    if len_i > 10:
         i = i[:10]+"..."
         len_i = len(i)
# print(("-" * (15 - len_i)), sep='', end='+', flush=True)
    if idx == 0:
        ramka1 = ("+"+("-" * 14 ))*len_list+"+\n"
    else:
        ramka1 = ""
    if idx == len_list-1:
        ramka3 = "|"
        ramka2 = "\n"+("+"+("-" * 14))*len_list+"+\n"
    else:
        ramka2= ""
        ramka3= ""
    print((ramka1+"|" + i + (" " * (14 - len_i))+ramka3+ramka2), sep='', end='', flush=True)


# 3) Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 wydając ich jak najmniej.

def wylicz_monety(kwota):
    kwota = float(kwota)
    kwota = round(kwota * 100)
    monet_list = ['5zl', '2zl', '1zl', '50gr', '20gr', '10gr', '5gr', '2gr', '1gr']
    val_list = [500, 200, 100, 50, 20, 10, 5, 2, 1]

    for (i, j) in zip(monet_list, val_list):
        if kwota != 0:
            ile_monet = kwota // j
            print(i + ": " + ile_monet.__str__())
            kwota = kwota - ((kwota // j)*j)
licznik=0

while licznik <1:
    input_kwota = input("Wpisz kwotę: ")
    input_ver = input_kwota.replace('.', '')
    if input_ver.isdigit():
        wylicz_monety(input_kwota)
        licznik+=1
    else:
        print("Niewłaściwy parametr, podaj liczbę")

# 4) Program rysujący piramidę o określonej wysokości, np dla 3
#       #
#      ###
#     #####
def piramida(liczba_wierszy):
    for i in range(liczba_wierszy):
        print(' '*(liczba_wierszy-i-1) + '#'*(2*i+1))
licznik=0

while licznik<1:
    input_liczba=input("Wpisz liczbę całkowitą: ")
    if input_liczba.isdigit():
        liczba = int(input_liczba)
        piramida(liczba)
        licznik += 1
    else:
        print("Niewłaściwy parametr, podaj liczbę całkowitą")


# 5) Kalkulator do wyliczania wieku psa.
#    Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
#    Np: 15 ludzkich lat to 73 psie lata
def wylicz_wiek_psa(lata):
    psi_wiek=0
    for i in range(lata):
        if i < 2:
            psi_wiek = psi_wiek + 10.5
        else:
            psi_wiek = psi_wiek + 4
    print(psi_wiek)

licznik=0

while licznik <1:
    input_wiek = input("Wpisz wiek: ")
    if input_wiek.isdigit():
        wiek_x=int(input_wiek)
        wylicz_wiek_psa(wiek_x)
        licznik+=1
    else:
        print("Niewłaściwy parametr, podaj wiek jako liczbę całkowitą")

# 6) Stworzenie "programu nakładki" na dotychczasowe programiki.
#    Po wyborze danego programu z "menu" uruchomi się odpowiedni i po wykonaniu danej operacji zapyta czy wykonać inny program.
#    Sugeruje by każdy "podprogram był oddzielną funkcją".
#    Miejmy na uwadze to by w przyszłości ten program rozwijać podpinając kolejny "podprogram"
#    - powinno to być najprostsze jak się da (np tylko zmiana menu i jakiegoś jednego ifa?:) )
#    Przykład przy uruchomieniu:
#    "
#    Witaj w Multitool Python Program by iSA - wersja beta ;)
#    Wybierz program który cię interesuje:
#    1) Rysowanie kwadratu o zadanych parametrach
#    2) Rysowanie piramidy o określonej wysokości
#    3) Rozmienianie pieniędzy
#    4) Przeliczanie F->C
#    5) Przeliczanie C->F
#    6) ...
#    7) ...
#    R) Wybierz program losowo bo nie wiem czego szukam:)
#    X) Wyjście z programu
#    Twój wybór: _
#    "
#TBD