# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)
# input_cel=input("Podaj stopnie Celsjusza: ")
# st_cel = float(input_cel)
# st_far=(st_cel * 9/5) + 32
# print("Fahrenheit = (Celsjusz * 9/5) + 32")
# print("Fahrenheit = ("+st_cel.__str__()+" * 9/5) + 32")
# print("Stopnie Farenheita przy "+st_cel.__str__()+" stopniach Celsjusza = "+st_far.__str__())

# 2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
# input_far=input("Podaj stopnie Farenheita: ")
# st_far = float(input_far)
# st_cel=(st_far - 32) * 5/9
# print("Celsjusz = (Farenheit - 32) * 5/9")
# print("Celsjusz = ("+st_far.__str__()+" - 32) * 5/9")
# print("Stopnie Celsjusza przy "+st_far.__str__()+" stopniach Farenheita = "+st_cel.__str__())

# 3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
# input_r = input("Podaj długość promienia: ")
# val_r = float(input_r)
# val_pi = 3.14
# print("Pole koła = Pi * r^2")
# print("Pole koła = 3.14 * " + val_r.__str__())
# val_pk = val_pi * (val_r * val_r)
# print("Pole koła = " + val_pk.__str__())

# 4. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
# input_l = input("Podaj liczbę: ")
# val_l = int(input_l)
# print("Podano liczbę " + val_l.__str__())
# val_pierwsza = int(str(val_l)[0])
# val_ostatnia = int(str(val_l)[-1])
# print("Pierwsza cyfra: " + val_pierwsza.__str__()+", ostatnia cyfra:"+val_ostatnia.__str__())

# 5. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
#     | (bok)
#     - (góra/dół)
#     + (wierzchołek)
#     czyli np:
#     +-------+
#     |       |
#     |       |
#     +-------+
in_pio = input("Długość pionowo:")
in_poz = input("Długość poziomo:")
val_pio = int(in_pio)
val_poz = int(in_poz)
str_poz = "-"*val_poz
str_spa = " "*val_poz
str_pio = ("\n|"+str_spa+"|")*val_pio
str_gra = ("+"+str_poz+"+")
print(str_gra + str_pio + "\n" + str_gra)
# 6. Napisz do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny. Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.
# 7. Napisz program do rozpoznawania czy podane liczba jest parzysta czy nie.
# 8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7
# 9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7
# 10. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym
#
# Podpowiedź: W zadaniach 7-10 należy użyć instrukcji warunkowych, wierzę że sobie poradzicie :)
# Podpowiedź: Wzory potrzebne do wyliczeń w niektórych zadaniach na pewno znajdziecie w internecie, jeśli nie to zapraszam na Slacka.
# Podpowiedź: Przypominam że stringi można mnożyć przez liczbę.
# Podpowiedź: Warto zobaczyć jeszcze jakie wbudowane metody posiadają stringi.
