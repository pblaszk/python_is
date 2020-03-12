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
# def hej(imie, nazwisko):
#     print(f'Dzień dobry {imie} {nazwisko}')
#
# hej("Piotr", "Błaszkiewicz")
