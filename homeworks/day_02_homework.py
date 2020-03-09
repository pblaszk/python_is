# import calendar
# #Piotr Blaszkiewicz
# # 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)
input_cel=input("Podaj stopnie Celsjusza: ")
st_cel = float(input_cel)
st_far=(st_cel * 9/5) + 32
print("Fahrenheit = (Celsjusz * 9/5) + 32")
print("Fahrenheit = ("+st_cel.__str__()+" * 9/5) + 32")
print("Stopnie Farenheita przy "+st_cel.__str__()+" stopniach Celsjusza = "+st_far.__str__())
#
# # 2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
input_far=input("Podaj stopnie Farenheita: ")
st_far = float(input_far)
st_cel=(st_far - 32) * 5/9
print("Celsjusz = (Farenheit - 32) * 5/9")
print("Celsjusz = ("+st_far.__str__()+" - 32) * 5/9")
print("Stopnie Celsjusza przy "+st_far.__str__()+" stopniach Farenheita = "+st_cel.__str__())
#
# # 3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
input_r = input("Podaj długość promienia: ")
val_r = float(input_r)
val_pi = 3.14
print("Pole koła = Pi * r^2")
print("Pole koła = 3.14 * " + val_r.__str__()+"^2")
val_pk = val_pi * (val_r * val_r)
print("Pole koła = " + val_pk.__str__())
#
# 4. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
input_l = input("Podaj liczbę: ")
val_l = int(input_l)
print("Podano liczbę " + val_l.__str__())
val_pierwsza = int(str(val_l)[0])
val_ostatnia = int(str(val_l)[-1])
print("Pierwsza cyfra: " + val_pierwsza.__str__()+", ostatnia cyfra:"+val_ostatnia.__str__())
#
# # 5. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
# #     | (bok)
# #     - (góra/dół)
# #     + (wierzchołek)
# #     czyli np:
# #     +-------+
# #     |       |
# #     |       |
# #     +-------+
in_pio = input("Długość pionowo:")
in_poz = input("Długość poziomo:")
val_pio = int(in_pio)
val_poz = int(in_poz)
str_poz = "-"*val_poz
str_spa = " "*val_poz
str_pio = ("\n|"+str_spa+"|")*val_pio
str_gra = ("+"+str_poz+"+")
print(str_gra + str_pio + "\n" + str_gra)
#
# # 6. Napisz do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# #Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.
in_bin = input("Podaj wartość binarną, 6 znaków: ")
out_val_1 = int(str(in_bin)[0])*2**5
out_val_2 = int(str(in_bin)[1])*2**4
out_val_3 = int(str(in_bin)[2])*2**3
out_val_4 = int(str(in_bin)[3])*2**2
out_val_5 = int(str(in_bin)[4])*2**1
out_val_6 = int(str(in_bin)[5])*2**0

print(out_val_1+out_val_2+out_val_3+out_val_4+out_val_5+out_val_6)

#
# # 7. Napisz program do rozpoznawania czy podane liczba jest parzysta czy nie.
in_num=input("Podaj dowolną liczbę całkowitą: ")
in_val = int(in_num)
if (in_val % 2) == 0:
    print("Liczba parzysta")
else:
    print("Liczna nieparzysta")
#
#  8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7
in_num=input("Podaj dowolną liczbę całkowitą: ")
in_val = int(in_num)

if (in_val % 3)  == 0 or (in_val % 5) == 0 or (in_val % 7) == 0:
    print("Liczba podzielna przez 3 lub 5 lub 7")
else:
    print("Liczba niepodzielna przez 3 lub 5 lub 7")
#
# 9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7
in_num=input("Podaj dowolną liczbę całkowitą: ")
in_val = int(in_num)
if (in_val % 3) == 0 and (in_val % 5) == 0 and (in_val % 7) == 0:
    print("Liczba podzielna przez 3 i 5 i 7")
else:
    print("Liczba niepodzielna przez 3 i 5 i 7")
#
# 10. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym
in_year=input("Podaj rok: ")
ch_year = int(in_year)
print(calendar.isleap(ch_year))
#
# #
# # Podpowiedź: W zadaniach 7-10 należy użyć instrukcji warunkowych, wierzę że sobie poradzicie :)
# # Podpowiedź: Wzory potrzebne do wyliczeń w niektórych zadaniach na pewno znajdziecie w internecie, jeśli nie to zapraszam na Slacka.
# # Podpowiedź: Przypominam że stringi można mnożyć przez liczbę.
# # Podpowiedź: Warto zobaczyć jeszcze jakie wbudowane metody posiadają stringi.
