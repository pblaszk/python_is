import requests
import json
import bs4
import copy
#strona = requests.get('https://wp.pl')
#dane = requests.get('https://api.exchangeratesapi.io/latest')
#print(dane.text)
# dane_str = dane.text
# dane_json = dane.json()
# print(type(dane_json))
#to jest juz slownik

# dane_json = json.loads(dane_str)
# print(dane_json['rates']['PLN'])
# olx_html = requests.get('https://www.olx.pl/motoryzacja/samochody/')
# parser = bs4.BeautifulSoup(olx_html.text, 'html.parser')
# obrazki = parser.find_all('img')
# for idx, obrazek in enumerate(obrazki):
#
#     #print(obrazek.get('alt'))
#     obrazekurl = (obrazek.get('src'))
#     nazwa = (obrazek.get('alt'))
#     print(nazwa)
#     print(obrazekurl)
#     if idx == 0:
#         obrazek = requests.get(obrazekurl).content
#         with open(f'zdjecie{idx}.jpg', 'wb') as plik:
#             plik.write(obrazek)

    #tworze katalog obrazki
    #sciagam obrezek z internetu
    #zapisuje jego zawrtosci do pliku NAZWA.JPG
    #gdzie NAZWA to wartość a <img 'alt'='...'>

    # with open('pic1.jpg', 'wb') as handle:
    #     response = requests.get(pic_url, stream=True)
    #
    #     if not response.ok:
    #         print
    #         response
    #
    #     for block in response.iter_content(1024):
    #         if not block:
    #             break
    #
    #         handle.write(block)

# imie='Piotrek'
# print(imie[2])      #o
# print(imie[:2])     #Pi
# print(imie[-2])     #e
# print(imie[1:2])    #io
# print(imie[1:5:2])  #it
# print(imie[::1])    #Piotrek
# print(imie[::-1])   #kertoiP
# ranga=range(0,12,3)
# for i in ranga:
#     print(i)

# lista = [ [1,2,3],[4,5,6],[7,8,9] ]
#
# print(lista[1][2]) #6
# print(lista[0][0]) #1

# wyrazy = ("raz", "dwa", "trzy")
# wyrazy[0] = "jeden"
# print(wyrazy)

# lista=["HEJKA", "OKEJKA"]
# print(lista)
# nowa_lista=lista.copy()
# #nowa_lista=list(lista)
# nowa_lista=lista[:]
# print(nowa_lista)
# najnowsza_lista=copy.deepcopy(lista)
# print(najnowsza_lista)
#
# osoby = {"studenci": ["Ala", "Jan", "Ania"],
#          "wykladowcy": ["doktor", "profesor"]}
# print(osoby["studenci"][1])#Jan
# osoby["wykladowcy"].append("magister")
# osoby["administracja"] = ["pani Basia z dziekanatu"]
# osoby.update({"ochrona":"Impel"})
# print(osoby.keys())
# print(osoby.values())
# for key, item in osoby.items():
#     print(key, item)

# wynik = 5 != 4 and 'a' not in 'Andrzej'
# print(wynik)#true