#pliki
#tryb w+ tylko wtedy gdy wiemy, ze plik nie istnieje
#tryb r najbezpieczniejszy, tryb r+ dobry, bo mozna zapisywac
#tryb a append ustawia sie na koncu
#tryb binarny dodac b
# plik = open('test.txt', 'rb+')
# print(plik.tell())
# print(plik.readline(), end = '')
# print(plik.tell())
# print(plik.seek(4, 1))
# print(plik.readline(), end = '')
# plik.close()

#nowa linia
# with open('test.txt', 'r') as plik:
#     print(plik.tell())
#     wszystkie_linie = plik.readlines()
#     print(wszystkie_linie)
#     print(plik.tell())
#     plik.write('linia 5')
import io

#kwestie uprawnien
# with open('test.txt', 'r') as plik:
#     print(plik.tell())
#     wszystkie_linie = plik.readlines()
#     print(wszystkie_linie)
#     print(plik.tell())
#     try:
#         plik.write('linia 5')
#     except io.UnsupportedOperation:
#         print('Nie masz uprawnien do zapisu')


# with open('test.txt', 'r+') as plik:
#     print(plik.tell())
#     wszystkie_linie = plik.readlines()
#     print(wszystkie_linie)
#     print(plik.tell())
#     try:
#         plik.write('\nlinia 6')
#     except io.UnsupportedOperation:
#         print('Nie masz uprawnien do zapisu')
#     print(plik.tell())
#def licz_uruchomienie()
#open('licznik.txt', 'w+')
#  as plik: print()

def licz_uruchomienie():
    try:
        with open('licznik.txt', 'r+') as plik:
            ilosc_uruchomien = plik.read()

            if ilosc_uruchomien == '':
                ilosc_uruchomien = 1
            else:
                ilosc_uruchomien = int(ilosc_uruchomien) + 1

            plik.seek(0)
            plik.write(str(ilosc_uruchomien))
            print(ilosc_uruchomien)
    except FileNotFoundError:
        with open('licznik.txt', 'w') as plik:
            plik.write("1")
            print("1")



licz_uruchomienie()
