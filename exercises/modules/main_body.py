import calendar
# #Piotr Blaszkiewicz
# day 02 homeworks
# # 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)
def st_cel_na_far(cel):
    st_cel = float(cel)
    st_far = (st_cel * 9 / 5) + 32
    print(f"Stopnie Farenheita przy " + st_far + " stopniach Celsjusza = " + st_cel)

# # 2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
def st_far_na_cel(far):
    st_far = float(far)
    st_cel = (st_far - 32) * 5 / 9
    print(f"Stopnie Farenheita przy " + st_cel + " stopniach Celsjusza = " + st_far)


# # 3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
def pole_kola(r):
    val_r = float(r)
    val_pi = 3.14
    val_pk = val_pi * (val_r * val_r)
    print("Pole koła = Pi * r^2")
    print("Pole koła = 3.14 * " + val_r + "^2")
    print(f"Pole koła = " + val_pk)


# 4. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
def pierwsza_ostatnia(val_l):
    val_pierwsza = str(val_l[0])
    val_ostatnia = str(val_l[-1])
    val_wynik = val_pierwsza + ", " + val_ostatnia
    print(f"Podano liczbę " + val_l)
    print(f"Pierwsza i ostatnia cyfra to: " + val_wynik)


# # 5. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
# #     | (bok)
# #     - (góra/dół)
# #     + (wierzchołek)
# #     czyli np:
# #     +-------+
# #     |       |
# #     |       |
# #     +-------+
def rysuj_prostokat(x, y):
    val_pio = int(y)
    val_poz = int(x)
    str_poz = "-" * val_poz
    str_spa = " " * val_poz
    str_pio = ("\n|" + str_spa + "|") * val_pio
    str_gra = ("+" + str_poz + "+")
    print(str_gra + str_pio + "\n" + str_gra)

#
# # 6. Napisz do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# #Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.
def bin_dzies(in_bin):
    out_val_1 = int(str(in_bin)[0])*2**5
    out_val_2 = int(str(in_bin)[1])*2**4
    out_val_3 = int(str(in_bin)[2])*2**3
    out_val_4 = int(str(in_bin)[3])*2**2
    out_val_5 = int(str(in_bin)[4])*2**1
    out_val_6 = int(str(in_bin)[5])*2**0
    print(out_val_1+out_val_2+out_val_3+out_val_4+out_val_5+out_val_6)


# # 7. Napisz program do rozpoznawania czy podane liczba jest parzysta czy nie.

def sprawdz_parzysta(in_int):
    in_val = int(in_int)
    if (in_val % 2) == 0:
        print("Liczba parzysta")
    else:
        print("Liczna nieparzysta")

#  8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7

def czy_podzielna_357lub(in_n8):
    in_val = int(in_n8)
    if (in_val % 3)  == 0 or (in_val % 5) == 0 or (in_val % 7) == 0:
        print("Liczba podzielna przez 3 lub 5 lub 7")
    else:
        print("Liczba niepodzielna przez 3 lub 5 lub 7")


# 9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7

def czy_podzielna_357i(in_n9):
    in_val = int(in_n9)
    if (in_val % 3) == 0 and (in_val % 5) == 0 and (in_val % 7) == 0:
        print("Liczba podzielna przez 3 i 5 i 7")
    else:
        print("Liczba niepodzielna przez 3 i 5 i 7")


# 10. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym
def sprawdz_rok_przestepny(y):
    ch_year = int(y)
    print(calendar.isleap(ch_year))


# 2) Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
#    Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
#    Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
#    A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn :)

def rysuj_liste(lista2):
    for idx, i in enumerate(lista2):
        len_i = len(i)
        len_list = len(lista2)
        if len_i > 10:
            i = i[:10] + "..."
            len_i = len(i)
        # print(("-" * (15 - len_i)), sep='', end='+', flush=True)
        if idx == 0:
            ramka1 = ("+" + ("-" * 14)) * len_list + "+\n"
        else:
            ramka1 = ""
        if idx == len_list - 1:
            ramka3 = "|"
            ramka2 = "\n" + ("+" + ("-" * 14)) * len_list + "+\n"
        else:
            ramka2 = ""
            ramka3 = ""
        print((ramka1 + "|" + i + (" " * (14 - len_i)) + ramka3 + ramka2), sep='', end='', flush=True)

#lista2 = [x for x in input("Podaj listę wartości, oddzielonymi spacją: ").split()]
#rysuj_liste(lista2)


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

# 4) Program rysujący piramidę o określonej wysokości, np dla 3
#       #
#      ###
#     #####
def piramida(liczba_wierszy):
    for i in range(liczba_wierszy):
        print(' '*(liczba_wierszy-i-1) + '#'*(2*i+1))

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

