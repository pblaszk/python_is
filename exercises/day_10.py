# # class Ksiazka():
# #     def __init__(self, tytul, autor, ilosc_stron=100, cena=19.99):
# #         self.tytul = tytul
# #         self.ilosc_stron = ilosc_stron
# #         self.autor = autor
# #         self.cena = cena
# #         self.vat = 7
# #
# #     def __str__(self):
# #         return f"{self.tytul}, autor: {self.autor}"
# #
# #     def __len__(self):
# #         return  self.ilosc_stron
# #
# #     def __add__(self, other):
# #         return self.ilosc_stron
# #
# # class Ebook(Ksiazka):
# #     def __init__(self, autor, tytul):
# #         super().__init__(autor, tytul)
# #         self.format = 'pdf'
# #         self.vat = 23
# #
# # ksiazka = Ksiazka('Potop', 'Sienkiewicz', 300)
# # ksiazka2 = Ksiazka('Trylogia', 'Sienkiewicz', 1300)
# #
# # ebook_1 = Ebook()
# # print(ebook_1)
# #
# # wynik = ksiazka + string
# # class Zwierze(object):
# #     pass
# #
# # class Czlowiek(Zwierze):
# #     pass
# #
# # class Student(Czlowiek):
# #     pass
# #
# # class Kot(Zwierze):
# #     pass
# #
# # class Pies(Zwierze):
# #     pass
# #
# # class Bokser(Pies):
# #     pass
# #
# # class Jamnik(Pies):
# #     pass
#
# # class Zwierze(object):
# #     def hej(self):
# #         print('Heeej!')
# #
# # class Czlowiek(Zwierze):
# #     def hej(self):
# #         print('Siema czlowiek!')
# #
# #
# # class Student(Czlowiek):
# #     def hej(self):
# #         print('Panda 3')
# #
# #
# # class Profesor(Czlowiek):
# #     def hej(self):
# #         print('Dzien dobry Panstwu!')
# #
# # zwierze = Zwierze()
# # zwierze.hej()
# # profesor = Profesor()
# # profesor.hej()
#
# # class C(object):
# #     def witaj(self):
# #         print('Jestem C')
# #
# # class D(B, C):
# #     def witaj(self):
# #         print('Jestem D')
# # class Z():
# #     pass
#
# # koszyk = Koszyk()
# # ksiazka_1 = Ksiazka('Potop'....)
# # koszyk.dodaj(ksiazka_1)
# # koszyk.dodaj(ksiazka_2)
# # koszyk.dodaj(ebook_1)
# # print("Ilosc w koszyku: " + len(koszyk))
# # print("Wartość netto: " + len(koszyk.wartosc_netto()))
# # print("Wartość brutto: " + len(koszyk.wartosc_brutto()))
#
# class Ksiazka(object):
#     def __init__(self, tytul, autor, ilosc_stron=100, cena=19.99):
#         self.tytul = tytul
#         self.ilosc_stron = ilosc_stron
#         self.autor = autor
#         self.cena = cena
#         self.vat = 7
#     def __str__(self):
#         return f"{self.tytul}, autor: {self.autor}"
#     def __len__(self):
#         return self.ilosc_stron
#     def __add__(self, other):
#         if isinstance(other, Ksiazka):
#             return self.ilosc_stron + other.ilosc_stron
#         else:
#             print('Tak naprawdę nie dodałem nic')
#             return self.ilosc_stron
# class Ebook(Ksiazka):
#     def __init__(self, autor, tytul):
#         super().__init__(autor, tytul)
#         self.format = 'pdf'
#         self.vat = 23
#
# #ilosc
# #wartosc brutto
# #wartosc netto
# #elementy
# class Koszyk():
#     def __init__(self):
#         self.elementy = []
#         self.ilosc_elementow = 0
#         self.wartosc_brutto = 0
#         self.wartosc_netto = 0
#
#     def dodaj(self, element):
#         self.elementy.append(element)
#
#     def __len__(self):
#         return len(self.elementy)
#
#     def netto(self, ):
#
#     def brutto(self):
#
# koszyk = Koszyk()
# ksiazka1 = Ksiazka('Potop', 'Sienkiewicz', 300)
# ksiazka2 = Ksiazka('Trylogia', 'Sienkiewicz', 1300)
# ebook_1 = Ebook('Potop', 'Sienkiewicz')
#
# koszyk.dodaj(ksiazka1)
# koszyk.dodaj(ksiazka2)
# koszyk.dodaj(ebook_1)
#
#
#
#
