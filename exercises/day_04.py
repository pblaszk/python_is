#day 04
# lista = [1, 2, 3]
# nowa_lista = lista
# print(lista)
# lista[0] = 'jeden'
# print(nowa_lista)

#kopiowanie to snapshot nie jest referencyjne
# lista = ['A', 'B', 'C']
# oryginalna_kopia = lista.copy()
# print(lista)
# lista[0] = '1'
# print(oryginalna_kopia)
# print(lista)

#lista zagniezdzone
# lista = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# nowa_lista = lista
# print(lista[1][1])
# lista[1][1] = 'X'
# print(lista[1][1])
# print(nowa_lista[1][1])

#lista zagniezdzone cd EGZAMIN
# lista = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# import copy
# nowa_lista = copy.deepcopy(lista)
# print(lista[1][1])
# lista[1][1] = 'X'
# print(lista[1][1])
# print(nowa_lista[1][1])

#funkcja
# def hej():
#     print('Dzień dobry')
#
# hej()
# dzien_dobry = hej
# dzien_dobry()

#funkcja z 1 parametrem
# def hej(imie):
#     print(f'Dzień dobry {imie}')
#
# hej("Piotr")

#funkcja z 2 parametrami
#argumenty sa wymagane i pozycyjne (odpowiednia kolejnosc) przy wywoływaniu funkcji
# def hej(imie, nazwisko):
#     print(f'Dzień dobry {imie} {nazwisko}')
#
# hej("Piotr", "Błaszkiewicz")

#funkcja z parametrem domyslnym
#mozna odwracac kolejnosc wywlowywania, ale przy wskazaniu, ktora wartosc do ktorej funkcji
# def hej(imie, nazwisko = "Błaszkiewicz"):
#      print(f'Dzień dobry {imie} {nazwisko}')
#
# hej("Piotr")
# hej(nazwisko="Kot", imie='Stefan')

#jesli wywloujemy ze wskazniem nazwy agrumentu, trzeba sie potem tego trzymac
# def hej(x, y, imie='Ola', wiek=18):
#     pass
# hej(1,2,imie="Gosia",wiek=22)

# def hej(x, y, imie='Ola', wiek=18):
#     pass
# hej(1,2,"Gosia",wiek=22)

#funkcja z dodawaniem
# def dodaj(x, y):
#     suma = float(x) + float(y)
#     return suma
#
# wynik = dodaj(3,7)
# print(wynik)

#funkcja, zmienne lokalne, globalne
# suma = 15
# def dodaj(x, y):
#     suma = float(x) + float(y)
#     return suma
#
# print(suma)
# suma = dodaj(2,7)
# print(suma)


