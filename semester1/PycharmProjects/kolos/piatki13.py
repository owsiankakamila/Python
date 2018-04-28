# piatek jest piatkiem 13 jesli pierwszym dniem danego miesiaca jest niedziela(7)

dni_w_miesiacu = [31,28,31,30,31,30,31,31,30,31,30,31]
nazwy_miesiecy = ["styczen", "luty", "marzec", "kwiecien", "maj", "czerwiec", "lipiec", "sierpien", "wrzesien", "pazdziernik", "listopad", "grudzien"]

rok = 2001
rok_stop = 2016
miesiac = 0
pierwszy_dzien_mies = 1

print("Piatki 13 w latach", rok, "-",rok_stop)

while rok<= rok_stop:
    miesiac=0

    if rok%4 ==0:
        dni_w_miesiacu[1] = 29
    else:
        dni_w_miesiacu[1] = 28

    while miesiac<12:
        if pierwszy_dzien_mies==7:
            print(nazwy_miesiecy[miesiac], rok)

        pierwszy_dzien_mies = pierwszy_dzien_mies + dni_w_miesiacu[miesiac]%7

        if pierwszy_dzien_mies >7:
            pierwszy_dzien_mies = pierwszy_dzien_mies -7

        miesiac+=1

    rok+=1
