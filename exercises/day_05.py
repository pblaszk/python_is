# #slownik
# slownik = {}
# slownik['imiona'] = ['Ala', 'Jan']
# slownik.update({'nazwiska': ['Kowalski', 'Malinowski']})
#
#
# wiersze = [
#     {'imie': 'Łukasz', 'nazwisko': 'Błaszkiewicz'},
#     {'imie': 'Adam', 'nazwisko': 'Kowalski'},
#     {'imie': 'Jan', 'nazwisko': 'Nowak'},
# ]
#
# slownik1 = {}
#
#
# #wyswietl element z listy
# for element in wiersze:
#    print(f"Mam na imie: {element['imie']}")
#
# #print(slownik1)

# slownik = {'imie': "Piotr", 0: 'Wartosc zero', "0": 'Wartosc zero stringiem'}
# print(slownik['imie'])
# print(slownik[0])
# print(slownik["0"])
# try:
#     wynik = 15/0
# except:
#     print('Wystąpił błąd')
# else:
#     print('Nie ma bledu')
# finally:
#     print('ZAWSZE')

# liczba = None
# while liczba is None:
#     wartosc = input('Podaj liczbe: ')
#     try:
#         wartosc = wartosc.replace(',', '.')
#         liczba = float(wartosc)
#         print(liczba)
#     except:
#         print('To nie jest liczba. Podaj jeszcze raz!')

# import modules.witacz as witacz
# #from modules.witacz import dzein_dobry
#
# witacz.dzein_dobry()
# witacz.hej()
#
# dzein_dobry()

# import modules.validator as validator
# validator.is_number(input("Podaj liczbę"))


