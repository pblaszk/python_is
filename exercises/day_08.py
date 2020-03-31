import requests
import json
import bs4

#strona = requests.get('https://wp.pl')
#dane = requests.get('https://api.exchangeratesapi.io/latest')
#print(dane.text)
# dane_str = dane.text
# dane_json = dane.json()
# print(type(dane_json))
#to jest juz slownik

# dane_json = json.loads(dane_str)
# print(dane_json['rates']['PLN'])
olx_html = requests.get('https://www.olx.pl/motoryzacja/samochody/')
parser = bs4.BeautifulSoup(olx_html.text, 'html.parser')
obrazki = parser.find_all('img')
for idx, obrazek in enumerate(obrazki):

    #print(obrazek.get('alt'))
    obrazekurl = (obrazek.get('src'))
    nazwa = (obrazek.get('alt'))
    print(nazwa)
    print(obrazekurl)
    if idx == 0:
        obrazek = requests.get(obrazekurl).content
        with open(f'zdjecie{idx}.jpg', 'wb') as plik:
            plik.write(obrazek)

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