print('Wybierz działanie 1. Dodawanie | 2. Odejmowanie | 3. Mnożenie | 4. Dzielenie | Wpisz dowolny znak aby wyjść')
men = str(input())
if '1' > men > '5':
    print('Wybrana została niepoprawna opcja!')
else:
    if men == '1':
        liczba1 = float(input('Podaj pierwszą liczbę: '))
        wyjscie = 0
        while wyjscie == 0:
            x = float(input('Podaj kolejną liczbę: '))
            liczba1 = liczba1 + x
            print(liczba1)
            wyjscie = 1
            odpd = str(input('Jeśli chcesz kontynuować działanie wpisz T lub t, jeśli chcesz wyjść wpisz dowolny znak'))
            if odpd == 'T' or odpd == 't':
                wyjscie = 0
    elif men == '2':
        liczba1 = float(input('Podaj pierwszą liczbę: '))
        wyjscie = 0
        while wyjscie == 0:
            x = float(input('Podaj kolejną liczbę: '))
            liczba1 = liczba1 - x
            print(liczba1)
            wyjscie = 1
            odpd = str(input('Jeśli chcesz kontynuować działanie wpisz T lub t, jeśli chcesz wyjść wpisz dowolny znak'))
            if odpd == 'T' or odpd == 't':
                wyjscie = 0
    elif men == '3':
        liczba1 = float(input('Podaj pierwszą liczbę: '))
        wyjscie = 0
        while wyjscie == 0:
            x = float(input('Podaj kolejną liczbę: '))
            liczba1 = liczba1 * x
            print(liczba1)
            wyjscie = 1
            odpd = str(input('Jeśli chcesz kontynuować działanie wpisz T lub t, jeśli chcesz wyjść wpisz dowolny znak'))
            if odpd == 'T' or odpd == 't':
                wyjscie = 0
    elif men == '4':
        liczba1 = float(input('Podaj pierwszą liczbę: '))
        wyjscie = 0
        while wyjscie == 0:
            x = float(input('Podaj kolejną liczbę: '))
            if x == 0:
                print('Nie dziel przez 0!')
            else:
                liczba1 = liczba1 / x
                print(liczba1)
                wyjscie = 1
                odpd = str(input('Jeśli chcesz kontynuować działanie wpisz T lub t, jeśli chcesz wyjść wpisz dowolny znak'))
                if odpd == 'T' or odpd == 't':
                    wyjscie = 0
    else:
        print('Dowidzenia!')