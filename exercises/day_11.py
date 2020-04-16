# class Tajny_agent():
#
#     def __init__(self, imie, nazwisko):
#         self.__imie = imie
#         self.__nazwisko = nazwisko
#         self.__zarobki = 9999
#
#     @property
#     def imie(self):
#         return self.__imie[0].capitalize() + "****"
#
# agent_1 = Tajny_agent('Tomek', 'Kowalski')
# print(agent_1.imie)

# Klasa Samochod z publicznymi własciwościami obiektu:
# marka, kolor, pojemnosc, cena_netto
# i z prywatnymi klasy maraza = 10%
# i z publiczna klasy vat = 23%
#
# I wyśweitlenie po utworzeniu obiektu:
# IN: Smochód('AUDI', 'BIAŁY', '100000.00')
# OUT: "Kupiłeś auto AUDI w kolorze BIAŁY za 199999.99zł brutto ";

class Samochod():

    stawka_vat = 1.23
    __marza = 1.10

    def __init__(self, marka, kolor, pojemnosc, cena_netto):
         self.marka = marka
         self.kolor = kolor
         self.pojemnosc = pojemnosc
         self.cena_netto = cena_netto

    @property
    def cena_auta(self):
        finalna_cena = int(self.cena_netto) * int(self.stawka_vat) + (int(self.cena_netto) + int(self.__marza))
        return finalna_cena

auto_1 = Samochod('AUDI', 'BIAŁY', '5', '100000.00')
print(auto_1.cena_auta)