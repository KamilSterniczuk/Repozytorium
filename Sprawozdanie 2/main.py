import pickle
import datetime
Data = datetime.datetime.now()
def MenuLista():
    Menu = str(input('1. Wyświetlanie Listy | 2. Dodawanie listy | 3. Edytowanie listy | 4. Czyszczenie listy | Wpisz dowolny znak aby wyjść '))
    Lista31 = [1, 3, 5, 7, 8, 10, 12]
    Lista30 = [4, 6, 9, 11]
    ListaTodo = []
    ListaTodo = pickle.load(open('TodoLista.dat', 'rb'))
    #Wypisywanie
    if Menu == '1':
        ListaTodo = pickle.load(open('TodoLista.dat', 'rb'))
        i = 0
        u = 0
        for i in range(0, int(len(ListaTodo) / 4)):
            print(i+1, ListaTodo[u],' ',ListaTodo[u+1],'-',ListaTodo[u+2],'-',ListaTodo[u+3])
            u += 4
        MenuLista()
    #Dodawanie
    elif Menu == '2':
        ListaTodo = pickle.load(open('TodoLista.dat', 'rb'))
        Tresc = str(input('Podaj treść: '))
        Rok = int(input('Podaj rok: '))
        if Data.year > Rok:
            print('Podano niepoprawny rok')
            MenuLista()
        else:
            Miesiac = int(input('Podaj miesiąc: '))
            if 1 > Miesiac or Miesiac > 12 and Miesiac > Data.month:
                print('Podano niepoprawny miesiąc')
                MenuLista()
            else:
                Dzien = int(input('Podaj dzień: '))
                if Dzien in range(1,31) and Miesiac in Lista31:
                        ListaTodo.append(Tresc)
                        ListaTodo.append(Dzien)
                        ListaTodo.append(Miesiac)
                        ListaTodo.append(Rok)
                        i = 0
                        u = 0
                        for i in range(0, int(len(ListaTodo) / 4)):
                            print(i + 1, ListaTodo[u], ' ', ListaTodo[u + 1], '-', ListaTodo[u + 2], '-', ListaTodo[u + 3])
                            u += 4
                        pickle.dump(ListaTodo, open('TodoLista.dat', 'wb'))
                elif Dzien in range(1,30) and Miesiac in Lista30:
                        ListaTodo.append(Tresc)
                        ListaTodo.append(Dzien)
                        ListaTodo.append(Miesiac)
                        ListaTodo.append(Rok)
                        i = 0
                        u = 0
                        for i in range(0, int(len(ListaTodo) / 4)):
                            print(i + 1, ListaTodo[u], ' ', ListaTodo[u + 1], '-', ListaTodo[u + 2], '-', ListaTodo[u + 3])
                            u += 4
                        pickle.dump(ListaTodo, open('TodoLista.dat', 'wb'))
                elif Dzien < 30 and Miesiac == 2 and Rok % 4 == 0:
                    if Dzien > 0:
                        ListaTodo.append(Tresc)
                        ListaTodo.append(Dzien)
                        ListaTodo.append(Miesiac)
                        ListaTodo.append(Rok)
                        i = 0
                        u = 0
                        for i in range(0, int(len(ListaTodo) / 4)):
                            print(i + 1, ListaTodo[u], ' ', ListaTodo[u + 1], '-', ListaTodo[u + 2], '-', ListaTodo[u + 3])
                            u += 4
                        pickle.dump(ListaTodo, open('TodoLista.dat', 'wb'))
                elif Dzien < 29 and Miesiac == 2 and Rok % 4 != 0:
                    if Dzien > 0:
                        ListaTodo.append(Tresc)
                        ListaTodo.append(Dzien)
                        ListaTodo.append(Miesiac)
                        ListaTodo.append(Rok)
                        i = 0
                        u = 0
                        for i in range(0, int(len(ListaTodo) / 4)):
                            print(i + 1, ListaTodo[u], ' ', ListaTodo[u + 1], '-', ListaTodo[u + 2], '-', ListaTodo[u + 3])
                            u += 4
                        pickle.dump(ListaTodo, open('TodoLista.dat', 'wb'))
                    else:
                      print('Wpisano niepoprawny dzień')
                      MenuLista()
                else:
                    print('Wpisano niepoprawny dzień')
                MenuLista()
    #Edytowanie
    elif Menu == '3':
        i = 0
        u = 0
        for i in range(0, int(len(ListaTodo) / 4)):
            print(i+1, ListaTodo[u],' ',ListaTodo[u+1],'-',ListaTodo[u+2],'-',ListaTodo[u+3])
            u += 4
        nr = int(input('Którą listę chciałbyś edytować? Podaj nr: '))

        x = str(input('Co chciałbyś edytować?: '))
        if x == 'Treść' or x == 'Tresc':
                x = nr * 4 - 4

        elif x == 'Dzień' or x == 'Dzien':
                x = nr * 4 - 3

        elif x == 'Miesiąc' or x == 'Miesiac':
                x = nr * 4 - 2

        elif x == 'Rok':
                x = nr * 4 - 1

        y = str(input('Podaj nowe dane: '))

        ListaTodo[x] = y

        pickle.dump(ListaTodo, open('TodoLista.dat', 'wb'))

        i = 0
        u = 0
        for i in range(0, int(len(ListaTodo) / 4)):
            print(i + 1, ListaTodo[u], ' ', ListaTodo[u + 1], '-', ListaTodo[u + 2], '-', ListaTodo[u + 3])
            u += 4
        MenuLista()

    #Usuwanie
    elif Menu == '4':
        ListaClear = str(input('Czy na pewno chcesz wyczyścić listę?: '))
        if ListaClear == 'Tak' or ListaClear == 'tak' or ListaClear == 'T' or ListaClear == 't':
            i = 0
            u = 0
            for i in range(0, int(len(ListaTodo) / 4)):
                print(i + 1, ListaTodo[u], ' ', ListaTodo[u + 1], '-', ListaTodo[u + 2], '-', ListaTodo[u + 3])
                u += 4
            listanr = int(input('Wybierz listę którą chcesz usunąć: '))
            NR = listanr * 4
            b = 0
            while 4 > b:
                b = b+1
                del ListaTodo[(NR - 4)]


            pickle.dump(ListaTodo, open('TodoLista.dat', 'wb'))
            print('Lista została wyczyszczona')
            MenuLista()
        else:
            print('Nic nie zostało usunięte')
            MenuLista()
    else:
        print('Dowidzenia!')
MenuLista()