def is_number(number):
        try:
            number = number.replace(',', '.')
            liczba = float(number)
            print(True)
        except:
            print(False)
