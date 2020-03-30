import openpyxl
import csv
# 17) Napisz program, który poda statystki dowolnego tekstu pobranego z pliku, wypisze takie dane jak, np:
#    ilość użyć poszczególnych literek i cyfr, ilość wyrazów, zdań etc.
#    Niech będzie możliwość wyboru tryb case sensitivity.
#    Niech program tworzy też plik ze statystyką swojej pracy. Czyli np:
#    "
#    Ilość uruchomień programu:
#    10
#    Przeanalizowanych znaków:
#    1223435991
#    Znalezionych wyrazów:
#    2399
#    Znalezionych liczb:
#    122
#    Znalezionych małych liter:
#    68923455
#    etc
#    "
# Oczywiście dopuszalna jest ułomność takiego programu.
#    Dokładne policzenie ilość zdań nie jest trywialne ale może jakiś fajny algorytm uda się Wam wymyślić.
#    Rodzaje statystyk zostawiam waszej fantazji :)
#    Przydatny generator tekstu: http://lipsum.pl/
# def zapisz_statystyki_pliku(stats_filename, lilosc_uruchomien, liczba_wyrazow, liczba_znakow):
#     with open(stats_filename, 'w+') as stats_plik:
#            stats_plik.seek(0)
#            stats_plik.write(f"Ilość uruchomień: \n"+str(lilosc_uruchomien)
#                       +"\nLiczba wyrazów: \n"+str(liczba_wyrazow)
#                             +"\nLiczba znaków: \n"+str(liczba_znakow))
#
#
# def pobierz_statystyki_pliku(filename):
#     report_filename = f'report_' + filename
#     try:
#         with open(filename, 'r+') as plik:
#             odczyt_pliku = plik.read()
#
#             try:
#                 with open(report_filename, 'r+') as raport:
#                     ilosc_uruchomien = raport.read().split('\n')[1]
#
#                     if ilosc_uruchomien == '':
#                         ilosc_uruchomien = 1
#                     elif ilosc_uruchomien.isdigit():
#                         ilosc_uruchomien = int(ilosc_uruchomien) + 1
#                     else:
#                         ilosc_uruchomien = 1
#             except FileNotFoundError:
#                 with open(filename, 'w') as plik:
#                     zapisz_statystyki_pliku(report_filename, 1, 1, 1)
#         liczba_wyrazow = len(odczyt_pliku.split())
#         liczba_znakow = len(odczyt_pliku) - odczyt_pliku.count(" ")
#         zapisz_statystyki_pliku(report_filename, ilosc_uruchomien, liczba_wyrazow, liczba_znakow)
#
#     except FileNotFoundError:
#         with open(filename, 'w') as plik:
#             zapisz_statystyki_pliku(report_filename, 1, 1, 1)
#
# pobierz_statystyki_pliku(input("Podaj nazwę i format pliku: "))

# 18) Stwórz program który przyjmie w parametrze ścieżkę do dowolnego pliku (CSV lub Excel - jaki wolicie), który będzie zawierał dane tabelaryczne.
#    W pliku pierwszy wiersz będzie zawierał nazwy kolumn a pozostałe wiersze dane.
#    Ilość kolum i wierszy może być dowolna. Program ma narysować tabelę z danymi, analogicznie do wcześniejszego zadania na rysowanie tabeli.
#    Pamiętajmy by wydzielać części reużywalne do oddzielnych funkcji/modułów (np.: odczyt danych, przygotowanie danych, rysowanie tabeli).
#    Przykład:
#    +------------+------------+------------+
#    | klucz1     | klucz 2    | klucz 3    |
#    +------------+------------+------------+
#    | row 1 col1 | row 1 col2 | row 1 col3 |
#    +------------+------------+------------+
#    | row 2 col1 | row 2 col2 | row 2 col3 |
#    +------------+------------+------------+
def tabela_z_pliku(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lista2=row
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


tabela_z_pliku('stolice.csv')
#
# 19) Zaskocz mnie :) Wymyśl swój własny program. Coś co np rozwiązuje Twój realny problem z pracy czy z życia codziennego.
#      Postarajcie się wymyśleć taki programik w którym użyjecie jak najwięcej poznanych rzeczy, np: łapanie wyjątków, pętle, operacje na plikach, korzystanie z nowych instalowanych z zewnątrz modułów etc.
#      Możecie też używać czegoś czego nie było na zajęciach (np kolorowanie tekstu w konsoli) a znaleźliście w internecie - byle byście rozumieli napisany kod :)
#      Przykłady: "zmieniacz - zmiana nazw wielu plików na raz", "kalambury - generator haseł", "enigma - szyfrowanie, odszyfrowywanie tekstu"...
#      Liczę na waszą inwencję, programy nie muszą być użyteczne - mogą być po prostu zabawne :)
#
# 20) Dodajcie do multitoola licznik wysyłań każdego podprogramu i samego multitoola. Dane możecie zapisać w dowolnym pliku CSV/pickle/Excel.
#      Do menu dodajcie pozycję/podprogramik "S - Statystyki" który w przyjaznej formie przedstawi wszystkie statystyki.
#
#
